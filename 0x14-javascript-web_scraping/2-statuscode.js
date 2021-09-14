#!/usr/bin/node

const request = require('request');

request(process.argv[2], (data) => {
  console.log('code:', data && data.statusCode);

  data.on('error', (e) => {
    console.error(e);
  });
});
