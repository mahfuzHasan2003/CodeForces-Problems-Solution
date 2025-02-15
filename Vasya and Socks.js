const readline = require("readline");

// Setup input handling
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputLines = [];

rl.on("line", (line) => {
  inputLines.push(line);
  // Once all input lines are received, process them
  if (inputLines.length === 1) {
    rl.close();
  }
});

rl.on("close", () => {
  // Parse input values
  const [n, m] = inputLines[0].split(" ").map(Number);
  // Call function to solve the problem
  const result = solution(n, m);
  console.log(result);
});

// ---------------------- Main solution of the problem ----------------------------
function solution(n, m) {
  let shocksLeft = n,
    totalDays = n;
  while (shocksLeft >= m) {
    totalDays += 1;
    shocksLeft = shocksLeft - m + 1;
  }
  return totalDays;
}
