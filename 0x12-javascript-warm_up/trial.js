#!/usr/bin/node
const num = 5;
let i = 0;
let symbol = null;
for (i = 1; i <= num; i++) {
  symbol = '';
  for (y = 0; y <= num; y++) {
    symbol += '#';
    }
  console.log(symbol)
}
