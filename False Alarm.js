const readline = require('readline');

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

let inputLines = [];

rl.on('line', function (line) {
   inputLines.push(line.trim());
});

function mainSolution(x, doors = []) {
   const minTimeToPass = doors.lastIndexOf(1) - doors.indexOf(1) + 1;
   return minTimeToPass <= x ? "YES" : "NO";
}

rl.on('close', function () {
   const t = parseInt(inputLines[0]);
   let line = 1;

   for (let i = 0; i < t; i++) {
      const [n, x] = inputLines[line++].split(' ').map(Number);
      const doors = inputLines[line++].split(' ').map(Number);
      console.log(mainSolution(x, doors));
   }
});
