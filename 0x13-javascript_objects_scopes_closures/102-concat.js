#!/usr/bin/node
// Defines a script that concats 2 files

// Import the fs module to work with the file system
const fs = require('fs');

// Get the file paths of the first source file, the second source file, and the destination from the command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read the contents of fileA and fileB using the readFile() method
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    // Handle any possible errors
    console.error(err);
  } else {
    // Read the contents of fileB
    fs.readFile(fileB, 'utf8', (err, dataB) => {
      if (err) {
        // Handle any possible errors
        console.error(err);
      } else {
        // Concat the contents of fileA and fileB using the + operator
        const dataC = dataA + dataB;
        // Write the concatenated data to fileC using the writeFile() method
        fs.writeFile(fileC, dataC, 'utf8', (err) => {
          if (err) {
            // Handle any possible errors
            console.error(err);
          }
        });
      }
    });
  }
});
