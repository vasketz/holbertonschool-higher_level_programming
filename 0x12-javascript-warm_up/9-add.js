#!/usr/bin/node
// this script prints the sum of two integers
const args = process.argv.slice(2);
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
}
add(args[0], args[1]);
