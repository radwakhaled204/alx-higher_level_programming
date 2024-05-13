#!/usr/bin/node
// This is a Node.js script that downloads a file from a given URL and saves it with a given name

// Import the fs module to access file system operations
const fs = require('fs');

// Import the request module to make HTTP requests
const request = require('request');

// Use the request method to get the data from the URL given as the first command line argument
// and pipe it to the createWriteStream method to save it as a file with the name given as the second command line argument
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
