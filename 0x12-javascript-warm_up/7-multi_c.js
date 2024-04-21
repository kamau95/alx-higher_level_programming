#!/usr/bin/node
const myDefault = 'Missing number of occurrences';
const myStr = 'C is fun';
const arg = process.argv[2];
let i = 0;
if (!isNaN(arg)) {
  for (i = 1; i <= arg; i++) {
    console.log(myStr);
  }
} else {
  console.log(myDefault);
}
