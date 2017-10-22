import { hash, BLOCK_BYTES } from './sha256';

function str2bytes(s) {
  let result = new Uint8Array(s.length);
  for (let i=0; i<s.length; i++)
    result[i] = s.charCodeAt(i);
  return result;
}

export function hmac(key, message) {
  if (typeof key === 'string')
    key = str2bytes(key);
  if (typeof message === 'string')
    message = str2bytes(message);
  let key2 = new Uint8Array(BLOCK_BYTES).fill(0);
  for (let i = 0; i < key.length && i < BLOCK_BYTES; i++)
    key2[i] = key[i];
  const o_key_pad = key2.map(k => 0x5c ^ k);
  const i_key_pad = key2.map(k => 0x36 ^ k);
  let first = new Uint8Array(BLOCK_BYTES + message.length);
  for (let i = 0; i < BLOCK_BYTES + message.length; i++)
    first[i] = (i < BLOCK_BYTES) ? i_key_pad[i] : message[i - BLOCK_BYTES];
  const res1 = hash(first);
  const second = new Uint8Array(BLOCK_BYTES + res1.length);
  for (let i=0; i< BLOCK_BYTES + res1.length; i++)
    second[i] = (i < BLOCK_BYTES) ? o_key_pad[i] : res1[i - BLOCK_BYTES];
  return hash(second);
}

