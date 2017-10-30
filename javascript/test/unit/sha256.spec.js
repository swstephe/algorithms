import { to_hex, hash } from '../../src/sha256';

const A_STR = "just a test string";

describe('sha256', () => {
  describe('#hash', () => {
    it('should return hash for empty string', () => {
      expect(to_hex(hash(''))).toBe('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855');
    });
    it('should return hash for a 1 character string', () => {
      expect(to_hex(hash('a'))).toBe('ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb');
    });
    it('should return hash for a 3 character string', () => {
      expect(to_hex(hash('abc'))).toBe('ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad');
    });
    it('should return hash for string with spaces', () => {
      expect(to_hex(hash(A_STR))).toBe('d7b553c6f09ac85d142415f857c5310f3bbbe7cdd787cce4b985acedd585266f');
    });
    it('should return hash for seven repeated string', () => {
      expect(to_hex(hash(A_STR.repeat(7)))).toBe('8113ebf33c97daa9998762aacafe750c7cefc2b2f173c90c59663a57fe626f21');
    });
    it('should return hash for twice repeated string', () => {
      expect(to_hex(hash(A_STR.repeat(2)))).toBe('03d9963e05a094593190b6fc794cb1a3e1ac7d7883f0b5855268afeccc70d461');
    });
    it('should return hash for 1 character', () => {
      expect(to_hex(hash('\xbd'))).toBe('68325720aabd7c82f30f554b313d0570c95accbb7dc4b5aae11204c08ffe732b');
    });
    it('should return hash for binary data', () => {
      expect(to_hex(hash('\xc9\x8c\x8e\x55'))).toBe('7abc22c0ae5af26ce93dbb94433a0e0b2e119d014f8e7f65bd56c61ccccd9504');
    });
    it('should return hash for 55 null bytes', () => {
      expect(to_hex(hash('\0'.repeat(55)))).toBe('02779466cdec163811d078815c633f21901413081449002f24aa3e80f0b88ef7');
    });
    it('should return hash for 56 null bytes', () => {
      expect(to_hex(hash('\0'.repeat(56)))).toBe('d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb');
    });
    it('should return hash for 57 null bytes', () => {
      expect(to_hex(hash('\0'.repeat(57)))).toBe('65a16cb7861335d5ace3c60718b5052e44660726da4cd13bb745381b235a1785');
    });
    it('should return hash for 64 null-bytes', () => {
      expect(to_hex(hash('\0'.repeat(64)))).toBe('f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b');
    });
    it('should return hash for 1000 null-bytes', () => {
      expect(to_hex(hash('\0'.repeat(1000)))).toBe('541b3e9daa09b20bf85fa273e5cbd3e80185aa4ec298e765db87742b70138a53');
    });
    it('should return hash for 1000 As', () => {
      expect(to_hex(hash('A'.repeat(1000)))).toBe('c2e686823489ced2017f6059b8b239318b6364f6dcd835d0a519105a1eadd6e4');
    });
    it('should return hash for 1005 Us', () => {
      expect(to_hex(hash('U'.repeat(1005)))).toBe('f4d62ddec0f3dd90ea1380fa16a5ff8dc4c54b21740650f24afc4120903552b0');
    });
  });
});
