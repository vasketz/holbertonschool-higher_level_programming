#!/usr/bin/node
// write a class rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let character = '';
    let col, row;
    for (col = 0; col < this.height; col++) {
      for (row = 0; row < this.width; row++) {
        character += 'X';
      }
      console.log(character);
      character = '';
    }
  }
};
