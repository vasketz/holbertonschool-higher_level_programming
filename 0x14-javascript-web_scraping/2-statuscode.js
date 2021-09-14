#!/usr/bin/node

const https = require('https');

https.get(process.argv[2], (data) => {
  console.log('code:', data && data.statusCode);

  data.on('error', (e) => {
    console.error(e);
  });
});
