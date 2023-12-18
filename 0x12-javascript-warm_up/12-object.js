#!/usr/bin/node
// This script updates an object to replace the value 12 with 89
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89; // Assign the new value 89 to the property value of the object
console.log(myObject);
