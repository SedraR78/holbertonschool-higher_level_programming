#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log("Missing size");
} else if (size > 0) {
  let row = 0;
  while (row < size) {
    let line = '';
    let col = 0;
    while (col < size) {
      line += 'X';
      col++;
    }
    console.log(line);
    row++;
  }
}
