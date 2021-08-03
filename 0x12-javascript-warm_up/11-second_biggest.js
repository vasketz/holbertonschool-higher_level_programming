#!/usr/bin/node
// this script searches or the second biggets integer
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  console.log(args.sort(function (n1, n2) { return n1 - n2; })[args.length - 2]);
}
