#!/usr/bin/node
// write a function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let index = 0;
  let i;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      index += 1;
    }
  }
  return index;
};
