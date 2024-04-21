#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
const erro = 'Missing size';
if (!isNaN(size)) {
  for (let i = 1; i <= size; i++) {
    let symbol = '';
    for (let j = 1; j <= size; j++) {
      symbol += 'x';
    }
    console.log(symbol);
  }
} else {
  console.log(erro);
}
