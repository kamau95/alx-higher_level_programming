#!/usr/bin/node
const arg = process.argv[2];
let converted = null;
if (!isNaN(arg)) {
  converted = parseInt(arg, 10);
  const printOut = 'My number: ' + converted;
  console.log(printOut);
} else {
  console.log('Not a number');
}
