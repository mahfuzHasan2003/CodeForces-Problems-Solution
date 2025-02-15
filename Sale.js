// Import necessary modules
const readline = require("readline");
// Setup input reading
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Read input
let inputLines = [];
rl.on("line", (line) => {
  inputLines.push(line);
  // Process input when all lines are received
  if (inputLines.length === 2) {
    rl.close();
  }
});

rl.on("close", () => {
  // Parse input values
  const [n, m] = inputLines[0].split(" ").map(Number);
  const prices = inputLines[1].split(" ").map(Number);

  // Call function to process data
  const result = solution(n, m, prices);
  console.log(result);
});

// --------------------------------------------------------------------
// NOTE: Main Code Here!!
function solution(n, m, prices = []) {
  const earnablePrice = prices
    .filter((p) => p < 0)
    .sort((a, b) => a - b)
    .slice(0, m);
  return earnablePrice.length === 0
    ? 0
    : Math.abs(earnablePrice.reduce((acc, cur) => acc + cur));
}
