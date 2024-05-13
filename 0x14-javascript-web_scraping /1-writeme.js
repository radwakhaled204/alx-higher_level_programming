#!/usr/bin/node
// This is a Node.js script that writes a file with the given name and content

// Import the fs module to access file system operations
const fs = require('fs');

// Use the writeFile method to create a file with
// the name and content from the command line arguments
fs.writeFile(process.argv[2], process.argv[3], error => {
  // If there is an error, log it to the console
  if (error) console.log(error);
});
