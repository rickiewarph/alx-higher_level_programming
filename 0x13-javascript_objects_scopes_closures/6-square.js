#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let m = 0; m < this.height; m++) {
      let y = '';
      for (let n = 0; n < this.width; n++) {
        y += c;
      }
      console.log(y);
    }
  }
}

module.exports = Square;
