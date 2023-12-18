#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments
const args = process.argv.slice(2); // Get the array of arguments passed to the script
if (args.length <= 1) { // If no argument or only one argument is passed
  console.log(0); // Print 0
} else { // Otherwise
  let max = -Infinity; // Initialize the maximum value to negative infinity
  let second = -Infinity; // Initialize the second maximum value to negative infinity
  for (let i = 0; i < args.length; i++) { // Loop through the array
    const num = parseInt(args[i]); // Try to convert each argument to an integer
    if (num > max) { // If the argument is greater than the maximum value
      second = max; // Update the second maximum value to the previous maximum value
      max = num; // Update the maximum value to the argument
    } else if (num > second && num < max) { // If the argument is between the maximum and the second maximum value
      second = num; // Update the second maximum value to the argument
    }
  }
  console.log(second); // Print the second maximum value
}
