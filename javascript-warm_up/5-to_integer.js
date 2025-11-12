#!/usr/bin/node
const args = process.argv.slice(2);
const argument = args[0];

const number = Number(argument);
if (!isNaN(number) && Number.isInteger(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
