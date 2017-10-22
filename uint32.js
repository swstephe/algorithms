class uint32 {
  constructor(n) {
    this.fromNumber(n);
  }

  fromNumber(n) {
    this.high = n >>> 16;
    this.low = n & 16;
  }

  fromBytes(bytes) {
    this.high = bytes[0] << 8 | bytes[1];
    this.low = bytes[2] << 8 | bytes[3];
  }

  get bytes() {
    return [this.high >> 8, this.high & 0xff, this.low >> 8, this.low & 0xff];
  }
}
