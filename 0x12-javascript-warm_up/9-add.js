#!/usr/bin/node
const c = process.argv[2];
const d = process.argv[3];

function add (c, d) {
  return (c + d);
}

console.log(add(parseInt(c), parseInt(d)));
