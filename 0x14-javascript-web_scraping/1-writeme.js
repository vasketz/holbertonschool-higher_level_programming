#!/usr/bin/node

const fs = require('fs');
const argpath = process.argv[2];
const texts = process.argv[3];

fs.writeFile(argpath, texts, 'utf-8', (err) => {
  if (err) {
    return console.log(err);
  }
});
