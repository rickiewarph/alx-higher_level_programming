#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let m = 0;
  while ((leng - m) > 0) {
    const aux = list[leng];
    list[leng] = list[m];
    list[m] = aux;
    m++;
    leng--;
  }
  return list;
};
