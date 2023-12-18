#!/usr/bin/node
// This script prints x times "C is fun"
// Get the first argument passed to the script
const arg = process.argv[2];
// Try to convert the argument to an integer
const x = parseInt(arg);
// If the argument is not a number
if (isNaN(x)) {
  // Print "Missing number of occurrences"
  console.log('Missing number of occurrences');
} else {
  // Otherwise Loop x times
  for (let i = 0; i < x; i++) {
    console.log('C is fun'); // Print "C is fun"
  }
}
