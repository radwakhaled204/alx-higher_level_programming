#!/usr/bin/node
// A script that displays the status code of a GET request.

// Import the request module
const request = require('request');

// Get the URL to request from the first argument
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (err, response, body) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, print the status code in the format: code: <status code>
    console.log(`code: ${response.statusCode}`);
  }
});
