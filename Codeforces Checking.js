const readline = require('readline');

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout,
})

let input = [];

rl.on('line', (line) => {
   input.push(line.trim());
});

rl.on('close', () => {
   const t = parseInt(input[0]);
   for (let i = 1; i <= t; i++) {
      const c = input[i];
      const target = "codeforces";
      if (target.includes(c)) {
         console.log("YES");
      } else {
         console.log("NO");
      }
   }
})
