#!/usr/bin/node
// This script prints the addition of 2 int
function add (a, b) {
  return a + b; // Return the sum of a and b
}

const arg1 = process.argv[2]; // Get the first argument passed to the script
const arg2 = process.argv[3]; // Get the second argument passed to the script
const num1 = parseInt(arg1); // Try to convert the first argument to an integer
const num2 = parseInt(arg2); // Try to convert the second argument to an integer
const result = add(num1, num2); // Call the function add with the integers
console.log(result); // Print the result
