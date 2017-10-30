import {BLOCK_BYTES, hash} from '../../src/sha256';
import { hmac } from '../../src/hmac';

function str2bytes(s) {
  let result = new Uint8Array(s.length);
  for (let i=0; i<s.length; i++)
    result[i] = s.charCodeAt(i);
  return result;
}

function hex2bytes(h) {
  let result = new Uint8Array(h.length / 2);
  for (let i=0; i<h.length; i+=2)
    result[i/2] = parseInt(h.substring(i, i+2), 16);
  return result;
}

describe('hmac', () => {
  it('step1', () => {
    let k1 = str2bytes('AWS4wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY');
    let key = new Uint8Array(BLOCK_BYTES).fill(0);
    for (let i=0; i<k1.length && i<BLOCK_BYTES; i++)
      key[i] = k1[i];
    let message = str2bytes('20150830');
    expect(key).toEqual(hex2bytes('41575334774a616c725855746e46454d492f4b374d44454e472b62507852666943594558414d504c454b45590000000000000000000000000000000000000000'));
    const o_key_pad = key.map(k => 0x5c ^ k);
    expect(o_key_pad).toEqual(hex2bytes('1d0b0f682b163d302e040928321a19111573176b111819121b773e0c240e3a351f0519041d110c10191719055c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c'));
    const i_key_pad = key.map(k => 0x36 ^ k);
    expect(i_key_pad).toEqual(hex2bytes('77616502417c575a446e63425870737b7f197d017b727378711d54664e64505f756f736e777b667a737d736f3636363636363636363636363636363636363636'));
    const first = new Uint8Array(BLOCK_BYTES + message.length);
    for (let i=0; i < BLOCK_BYTES + message.length; i++)
      first[i] = (i < BLOCK_BYTES) ? i_key_pad[i] : message[i - BLOCK_BYTES];
    expect(first).toEqual(hex2bytes('77616502417c575a446e63425870737b7f197d017b727378711d54664e64505f756f736e777b667a737d736f36363636363636363636363636363636363636363230313530383330'));
    const res1 = hash(first);
    expect(res1).toEqual(hex2bytes('f5b136e4b781f0ab4a59c845475237e283bdc5bfc0a3b25209a23a3e638af2b5'));
    const second = new Uint8Array(BLOCK_BYTES + res1.length);
    for (let i=0; i < BLOCK_BYTES + res1.length; i++)
      second[i] = (i < BLOCK_BYTES) ? o_key_pad[i] : res1[i - BLOCK_BYTES];
    expect(second).toEqual(hex2bytes('1d0b0f682b163d302e040928321a19111573176b111819121b773e0c240e3a351f0519041d110c10191719055c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5cf5b136e4b781f0ab4a59c845475237e283bdc5bfc0a3b25209a23a3e638af2b5'));
    const result = hash(second);
    expect(result).toEqual(hex2bytes('0138c7a6cbd60aa727b2f653a522567439dfb9f3e72b21f9b25941a42f04a7cd'));
  });
  it('step2', () => {
    let key = 'AWS4wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY';
    let message = '20150830';
    expect(hmac(key, message)).toEqual(hex2bytes('0138c7a6cbd60aa727b2f653a522567439dfb9f3e72b21f9b25941a42f04a7cd'));
  });
});
