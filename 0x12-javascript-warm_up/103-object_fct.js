#!/usr/bin/node
// This script updates an object by adding a new function incr that increments the integer value
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () { // Define a new function incr as a property of the object
  this.value++; // Increment the value of the object by one
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
