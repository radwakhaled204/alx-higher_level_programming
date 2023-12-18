#!/usr/bin/node
// Defines a script that imports an array and computes a new array

// Import the list from the file 100-data.js
const list = require('./100-data').list;

// Use a map to create a new array with each value equal to the value of the initial list, multiplied by the index in the list
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
