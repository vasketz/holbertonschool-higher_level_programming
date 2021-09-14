#!/usr/bin/node
// statusCode output from request

const request = require('request');
const url = process.argv[2]

request(url, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', data.statusCode);
  }
});
