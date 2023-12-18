#!/usr/bin/node
// This script prints the first argument passed to it
// Get the first argument passed
const arg = process.argv[2];
if (arg === undefined) {
  // if no argument is passed print 'No argument'
  console.log('No argument');
} else {
  // Otherwise print the argument
  console.log(arg);
}
