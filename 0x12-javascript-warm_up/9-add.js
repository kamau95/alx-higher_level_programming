#!/usr/bin/node
const arg1 = parseInt(process.argv[2], 10);
const arg2 =parseInt(process.argv[3], 10);
function add(a, b) {
  console.log(a + b);
  }
add(arg1, arg2);
