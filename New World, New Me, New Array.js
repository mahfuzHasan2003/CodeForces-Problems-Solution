const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  solve(input);
});

function mainSolution(n, k, p) {
  (n = Math.abs(n)), (k = Math.abs(k)), (p = Math.abs(p));

  if (n * p < k) return -1;
  return k % p === 0 ? k / p : Math.floor(k / p) + 1;
}
// console.log(mainSolution(21, 100, 10));
// console.log(mainSolution(9, -420, 42));

function solve(input) {
  let t = parseInt(input[0]); // Number of test cases

  for (let i = 1; i <= t; i++) {
    let [n, k, p] = input[i].split(" ").map(Number);
    console.log(mainSolution(n, k, p));
  }
}
