#!/usr/bin/node
// This script computes and prints a factorial
function factorial (n) {
  // If n is not a number or n is less than or equal to 1
  if (isNaN(n) || n <= 1) {
    return 1; // Return 1
  } else { // Otherwise
    // Return n multiplied by the factorial of n - 1 (recursive call)
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2]; // Get the first argument passed to the script
const num = parseInt(arg); // Try to convert the argument to an integer
const result = factorial(num); // Call the function factorial with the integer
console.log(result); // Print the result
