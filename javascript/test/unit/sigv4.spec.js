import {MockRequest} from './mock';
import * as sigv4 from '../../src/sigv4';

const config = {
  AWS_REGION: 'us-east-1',
  AWS_SERVICE: 'service',
  AWS_KEY: 'wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY'
};

const TESTS = [
  'get-header-key-duplicate',
  'get-header-value-multiline',
  'get-header-value-order',
  'get-header-value-trim',
  'get-unreserved',
  'get-utf8',
  'get-vanilla',
  'get-vanilla-empty-query-key',
  'get-vanilla-query',
  'get-vanilla-query-order-key',
  'get-vanilla-query-order-key-case',
  'get-vanilla-query-order-value',
  'get-vanilla-query-unreserved',
  'get-vanilla-utf8-query',
  'normalize-path/get-relative',
  'normalize-path/get-relative-relative',
  'normalize-path/get-slash',
  'normalize-path/get-slash-dot-slash',
  'normalize-path/get-slash-pointless-dot',
  'normalize-path/get-slashes',
  'normalize-path/get-space',
  'post-header-key-case',
  'post-header-key-sort',
  'post-header-value-case',
  // 'post-sts-token/post-sts-header-after',
  'post-sts-token/post-sts-header-before',
  'post-vanilla',
  'post-vanilla-empty-query-value',
  'post-vanilla-query',
  'post-x-www-form-urlencoded',
  'post-x-www-form-urlencoded-parameters'
];

// 'post-sts-token',


function load_file(url) {
  let req = new XMLHttpRequest();
  req.open('GET', url, false);
  req.send(null);
  if (req.readyState === 4) {
    if (req.status === 200) {
      return req.responseText;
    } else {
      console.error(url);
      console.error(req.statusText);
    }
  }
}

const is_whitespace = (ch) => ch === ' ' || ch === '\t';

function req_parse(text) {
  let req = new MockRequest('/');
  let i = 0;
  let k = 0;

  let name;
  let state = 'init';
  let done = false;
  for (let j = 0; j < text.length && !done; j++) {
    let ch = text.charAt(j);
    switch (state) {
      case 'init':
        if (ch === ' ') {
          req.method = text.substr(i, j - i);
          state = 'uri';
          i = j + 1;
        }
        break;
      case 'uri':
        if (is_whitespace(ch)) {
          k = j;
        } else if (ch === '?') {
          state = 'query';
        } else if (ch === '\n') {
          req.url = text.substr(i, k - i);
          i = j + 1;
          state = 'header-name';
        }
        break;
      case 'query':
        if (is_whitespace(ch)) {
          k = j;
        } else if (ch === '\n') {
          req.url = text.substr(i, k - i);
          i = j + 1;
          state = 'header-name';
        }
        break;
      case 'header-name':
        if (ch === ':') {
          state = 'header-value';
          name = text.substr(i, j - i);
          i = j + 1;
          while (is_whitespace(text.charAt(i)))
            i++;
        } else if (ch === '\n') {
          state = 'payload';
        } else if (is_whitespace(ch)) {
          state = 'header-value';
          i = j + 1;
          while (is_whitespace(text.charAt(i)))
            i++;
        }
        break;
      case 'header-value':
        if (ch === '\n') {
          state = 'header-name';
          req.headers.append(name, text.substr(i, j - i));
          i = j + 1;
        }
        break;
      case 'payload':
        req.body = text.substr(j);
        done = true;
        break;
      default:
        console.error("unhandled state="+state);
    }
  }
  if (state === 'header-value') {
    req.headers.set(name, text.substr(i));
  }
  return req;
}

describe('sigv4', () => {
  function test_steps(name) {
    let i = name.lastIndexOf('/');
    let basename = (i >= 0) ? name.substr(i+1) : name;
    let url = '/base/test/assets/aws_test_suite/' + name + '/' + basename;
    let req = req_parse(load_file(url +'.req'));
    let req_date = req.headers.get('X-Amz-Date');
    let CREQ_FILE = load_file(url + '.creq');
    let creq = sigv4.creq(req);
    expect(CREQ_FILE).toEqual(creq);
    let STS_FILE = load_file(url + '.sts');
    let sts = sigv4.sts(config, req_date, creq);
    expect(STS_FILE).toEqual(sts);
    let AUTHZ_FILE = load_file(url + '.authz');
    let authz = sigv4.authz(config, req_date, req, sts);
    expect(AUTHZ_FILE).toEqual(authz);
    let sreq = req_parse(load_file(url + '.sreq'));
    req.headers.append('Authorization', authz);
    expect(sreq).toEqual(req);
  }

  function test_all(name) {
    let i = name.lastIndexOf('/');
    let basename = (i >= 0) ? name.substr(i+1) : name;
    let url = '/base/test/assets/aws_test_suite/' + name + '/' + basename;
    let req = sigv4.signed(config, req_parse(load_file(url + '.req')));
    let sreq = req_parse(load_file(url + '.sreq'));
    expect(sreq).toEqual(req);
  }


  describe('signing', () => {
    it('should handle each signing step', () => {
      for (const test of TESTS) {
        test_steps(test);
      }
    });
    it('should sign requests', () => {
      for (const test of TESTS) {
        test_all(test);
      }
    });
  });
});
