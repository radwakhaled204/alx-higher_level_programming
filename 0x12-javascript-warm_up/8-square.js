#!/usr/bin/node
// This script that prints a square
// Get the first argument passed
const arg = process.argv[2];
// Try to convert the arg into an int
const size = parseInt(arg);
// If the argument is not a number print 'Missing size'
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Otherwise lopp size times
  for (let i = 0; i < size; i++) {
    // Initialize an emprt string for each row
    let row = '';
    // Loop size times
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
