#!/usr/bin/node
// write a class Square that defines a square and inherits from rectangle
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
