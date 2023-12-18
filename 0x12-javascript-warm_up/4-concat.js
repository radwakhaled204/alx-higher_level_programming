#!/usr/bin/node
// This script prints 2 arguments passed to it in the following format: " is "
// Get the first argument passed to the script
const arg1 = process.argv[2];
// Get the second argument passed to the script
const arg2 = process.argv[3];
// Print the arguments in the format " is "
console.log(arg1 + ' is ' + arg2);
