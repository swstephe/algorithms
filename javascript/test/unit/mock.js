export class MockHeaders {
  constructor(headers) {
    this.map = {};
    for (let name in headers) {
      if (headers.hasOwnProperty(name))
        this.map[name] = headers[name];
    }
  }

  append(name, value) {
    let oldValue = this.map[name];
    this.map[name] = oldValue ? oldValue + ',' + value : value;
  }

  get(name) {
    return this.map.hasOwnProperty(name) ? this.map[name] : null;
  }

  set(name, value) {
    let oldValue = this.map[name];
    this.map[name] = oldValue ? oldValue + ',' + value : value;
  }

  has(name) {
    return this.map.hasOwnProperty(name);
  }

  keys() {
    let items = [];
    for (let key in this.map) {
      if (this.has(key))
        items.push(key);
    }
    return items;
  }

  toString() {
    let items = [];
    for (let key in this.map) {
      if (this.map.hasOwnProperty(key)) {
        items.push(key + '=' + this.map[key]);
      }
    }
    return '{' + items.join(',') + '}';
  }
}

export class MockRequest {
  constructor(url, options) {
    options = options || {};
    this.method = options.method || 'GET';
    this.url = url;
    this.headers = new MockHeaders(options.headers);
    this.body = options.body || '';
  }

  text() {
    return this.body;
  }

  toString() {
    return 'MockRequest(url="'+this.url
    + '",method="'+this.method
    + '",headers='+this.headers
    + ',body="'+this.body+'")';
  }
}
