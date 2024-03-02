#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < x; a++) {
    let b = 0;
    let myVar = '';

    while (b < x) {
      myVar = myVar + 'X';
      b++;
    }
    console.log(myVar);
  }
}
