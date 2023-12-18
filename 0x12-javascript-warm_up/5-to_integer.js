#!/usr/bin/node
// This script prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer
// Get the first argument passed to the script
const arg = process.argv[2];
// Try to convert the argument to an integer
const num = parseInt(arg);
// If the argument is not a number Print "Not a number"
if (isNaN(num)) {
  console.log('Not a number');
} else {
  // Otherwise Print "My number: " followed by the integer
  console.log('My number: ' + num);
}
