const readline = require('readline');

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

let inputLines = [];
let currentLine = 0;

rl.on('line', (line) => {
   inputLines.push(line.trim());
});

rl.on('close', () => {
   main();
});

function readLine() {
   return inputLines[currentLine++];
}


// Main solution here
function makeSolution(number = 0) {
   let sqrt = Math.sqrt(number);
   if (!Number.isInteger(sqrt)) return -1;

   return sqrt % 2 === 0 ? `${sqrt / 2} ${sqrt / 2}` : `${Math.floor(sqrt / 2)} ${Math.ceil(sqrt / 2)}`

}

function main() {
   const t = parseInt(readLine());
   for (let i = 0; i < t; i++) {
      const s = readLine();
      console.log(makeSolution(parseInt(s)));
   }
}
