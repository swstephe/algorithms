import { hash, to_hex } from './sha256';
import { hmac } from './hmac';

export function reduce_uri(uri) {
  let stack = [];
  let pieces = uri.split('/');
  for (let i = 0, len=pieces.length; i < len; i++) {
    let piece = pieces[i];
    if (piece === '..')
      stack.pop();
    else if (piece === '' && i === len - 1)
      stack.push(piece);
    else if (piece !== '' && piece !== '.')
      stack.push(piece);
  }
  return '/' + stack.join('/');
}

export function encode_value(value) {
  value = encodeURI(value);
  let result = "";
  for (let i = 0, len=value.length; i<len; i++) {
    let ch = value.charCodeAt(i);
    result += (ch <= 32 || ch > 127) ? "%" + ("00"+ch.toString(16)).slice(-2) : value[i];
  }
  return result;
}

/**
 * Given an aurelia-http-client or aurelia-fetch-client, construct a "creq" buffer.
 * @param request -- the aurelia http/fetch client request
 */
export function creq(request) {
  let buffer = [];
  let i = request.url.indexOf('?');
  let uri = (i === -1) ? request.url  : request.url.slice(0, i);
  let query = (i === -1) ? '' : request.url.slice(i+1);
  query = query.split('&').sort().join('&');
  buffer.push(request.method);
  buffer.push(encodeURI(reduce_uri(uri)));
  buffer.push(encode_value(query));
  let keys = request.headers.keys();
  keys.sort();
  for (let key of keys) {
    buffer.push([
      key.toLowerCase(),
      request.headers.get(key).trim().replace(/\s+/g, ' ')
    ].join(':'));
  }
  buffer.push('');
  buffer.push(keys.map((name) => name.toLowerCase()).join(';'));
  buffer.push(to_hex(hash(request.text())));
  return buffer.join("\n");
}

export function sts(config, req_date, src) {
  let buffer = [];
  buffer.push('AWS4-HMAC-SHA256');
  buffer.push(req_date);
  buffer.push([
    req_date.substr(0, 8),
    config.AWS_REGION,
    config.AWS_SERVICE,
    'aws4_request'
  ].join('/'));
  buffer.push(to_hex(hash(src)));
  return buffer.join('\n');
}

function signing(config, req_date) {
  return (
    hmac(
      hmac(
        hmac(
          hmac("AWS4" + config.AWS_KEY, req_date.substr(0, 8)),
          config.AWS_REGION
        ),
        config.AWS_SERVICE
      ),
      'aws4_request'
    )
  )
}

export function authz(config, req_date, req, src) {
  let signature = hmac(signing(config, req_date), src);
  let buffer = [];
  buffer.push('Credential='+[
    'AKIDEXAMPLE',
    req_date.substr(0, 8),
    config.AWS_REGION,
    config.AWS_SERVICE,
    'aws4_request'
  ].join('/'));
  let keys = req.headers.keys();
  keys.sort();
  let headers = [];
  keys.forEach((k) => headers.push(k.toLowerCase()));
  buffer.push('SignedHeaders='+headers.join(';'));
  buffer.push('Signature='+to_hex(signature));
  return 'AWS4-HMAC-SHA256 ' + buffer.join(', ');
}

export function signed(config, req) {
  let req_date = req.headers.get('X-Amz-Date');
  req.headers.append(
    'Authorization',
    authz(
      config,
      req_date,
      req,
      sts(config, req_date, creq(req))
    )
  );
  return req;
}
