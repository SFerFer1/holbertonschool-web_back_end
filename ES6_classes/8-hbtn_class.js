export default class HolbertonClass {
    constructor(size, location) {
      this._size = size; // Store the size attribute
      this._location = location; // Store the location attribute
    }

    valueOf() {
      return this._size;
    }

    toString() {
      return this._location;
    }
  }
