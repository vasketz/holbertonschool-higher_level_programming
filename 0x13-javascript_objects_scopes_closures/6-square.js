#!/usr/bin/node
// write a class Square that defines a square and inherits from square
const Squar = require('./5-square');
module.exports = class Square extends Squar {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let character = '';
      let col, row;
      for (col = 0; col < this.height; col++) {
        for (row = 0; row < this.width; row++) {
          character += 'C';
        }
        console.log(character);
        character = '';
      }
    }
  }
};
