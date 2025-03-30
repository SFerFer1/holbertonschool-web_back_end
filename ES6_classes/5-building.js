export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw new Error(
        'Class extending Building must override evacuationWarningMessage' // Changed to single quotes
      );
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
