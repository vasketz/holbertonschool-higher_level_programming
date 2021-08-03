#!/usr/bin/node
// this script computes and print a factorial of a number
const args = process.argv.slice(2);
function factorial (args) {
  if (parseInt(args) === 0 || isNaN(args)) {
    return 1;
  } else {
    return args * factorial(args - 1);
  }
}
console.log(factorial(args[0]));
