#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const nDict = {};
for (const n in valsUniq) {
  const list = [];
  for (const v in totalist) {
    if (totalist[v][1] === valsUniq[n]) {
      list.unshift(totalist[v][0]);
    }
  }
  nDict[valsUniq[n]] = list;
}
console.log(nDict);
