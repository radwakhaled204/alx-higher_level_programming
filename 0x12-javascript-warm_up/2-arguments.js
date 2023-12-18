#!/usr/bin/node
// This script prints a message depending on the number of arguments passed
// Get the arrage of arguments passed
const args = process.argv.slice(2);
// If no args are passed print "No argument"
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  // if only one argument is passed print"Argument found"
  console.log('Argument found');
} else {
  // Otherwise Print "Arguments found"
  console.log('Arguments found');
}
