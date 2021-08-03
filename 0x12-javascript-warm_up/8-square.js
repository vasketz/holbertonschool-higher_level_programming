#!/usr/bin/node
// this script prints a square
const args = process.argv.slice(2);
if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  let col, row;
  let character = '';
  for (col = 0; col < args; col++) {
    for (row = 0; row < args; row++) {
      character += 'X';
    }
    console.log(character);
    character = '';
  }
}
