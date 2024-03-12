#!/usr/bin/node
let nargmnt = 0;

exports.logMe = function (item) {
  console.log(nargmnt + ': ' + item);
  nargmnt++;
};
