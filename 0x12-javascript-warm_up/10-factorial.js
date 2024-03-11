#!/usr/bin/node
function factorial (j) {
  if (j < 0) {
    return (-1);
  }
  if (j === 0 || isNaN(j)) {
    return (1);
  }
  return (j * factorial(j - 1));
}

console.log(factorial(Number(process.argv[2])));
