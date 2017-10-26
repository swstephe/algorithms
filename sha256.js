const H = new Uint32Array([
  0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
  0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]);
const K = new Uint32Array([
  0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
  0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
  0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
  0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
  0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
  0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
  0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
  0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
  0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
  0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
  0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
  0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
  0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
  0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
  0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
  0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]);
const HEX_DIGITS = "0123456789abcdef";
export const BLOCK_BYTES = 64;
const BLOCK_WORDS = BLOCK_BYTES / 4;

function uint32(x) {
  return (x & 0xffffffff) >>> 0;
}

function rotr(x, y) {
  return uint32((x >>> y) | (((x&(2**y - 1)) << (32 - y))));
}

function ch(x, y, z) {
  return z ^ (x & (y ^ z));
}

function maj(x, y, z) {
  return ((x | y) & z) | (x & y);
}

function sigma0(x) {
  return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22);
}

function sigma1(x) {
  return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25);
}

function sig0(x) {
  return rotr(x, 7) ^ rotr(x, 18) ^ (uint32(x) >>> 3);
}

function sig1(x) {
  return rotr(x, 17) ^ rotr(x, 19) ^ (uint32(x) >>> 10);
}

export function from_words(words) {
  let buf = new Uint8Array(words.length*4);
  let j = 0;
  for (let w of words) {
    buf[j++] = (w >>> 24) & 0xff;
    buf[j++] = (w >>> 16) & 0xff;
    buf[j++] = (w >>> 8) & 0xff;
    buf[j++] = w & 0xff;
  }
  return buf;
}

export function to_words(bytes) {
  let buf = new Uint32Array(BLOCK_WORDS).fill(0);
  let j = 0;
  for (let i=0; i<bytes.length; i+=4)
    buf[j++] = bytes.slice(i, i + 4).reduce((a, b) => a << 8 | b, 0);
  return buf;
}

export function from_string(s) {
  let result = new Array(s.length);
  for (let i=0; i<s.length; i++)
    result[i] = s.charCodeAt(i);
  return result;
}

export function to_hex(bytes) {
  let result = '';
  for (let i=0; i<bytes.length; i++)
    result += HEX_DIGITS.charAt(bytes[i] >>> 4 & 0xf) + HEX_DIGITS.charAt(bytes[i] & 0xf);
  return result;
}

export function hash(message) {
  if (typeof message === 'string')
    message = from_string(message);
  const count = message.length;
  const L = (count + 1) / 4 + 2;
  const N = Math.ceil(L / BLOCK_WORDS);
  let msg = new Uint8Array(N*BLOCK_BYTES);
  for (let i=0; i<message.length; i++)
    msg[i] = message[i];
  msg[message.length] = 0x80;
  let M = new Array(N);
  for (let i=0; i < N; i++)
    M[i] = to_words(msg.slice(i*BLOCK_BYTES, (i + 1)*BLOCK_BYTES));
  let last = M[M.length - 1];
  last[14] = count >>> 29;
  last[15] = uint32(count << 3);
  M[M.length - 1] = last;

  let W = new Array(BLOCK_BYTES);
  let t1, t2;
  let _H = H.slice();
  for (let i=0; i < N; i++) {
    for (let t=0;t<16;t++)
      W[t] = M[i][t];
    for (let t=16;t<BLOCK_BYTES; t++)
      W[t] = uint32(sig1(W[t - 2]) + W[t - 7] + sig0(W[t - 15]) + W[t - 16]);
    let a = _H[0];
    let b = _H[1];
    let c = _H[2];
    let d = _H[3];
    let e = _H[4];
    let f = _H[5];
    let g = _H[6];
    let h = _H[7];
    for (let j=0; j<BLOCK_BYTES; j++) {
      t1 = h + sigma1(e) + ch(e, f, g) + K[j] + W[j];
      t2 = sigma0(a) + maj(a, b, c);
      h = g;
      g = f;
      f = e;
      e = d + t1;
      d = c;
      c = b;
      b = a;
      a = uint32(t1 + t2);
    }
    _H = [a, b, c, d, e, f, g, h].map((e, i) => uint32(_H[i] + e));
  }
  return from_words(_H);
}
