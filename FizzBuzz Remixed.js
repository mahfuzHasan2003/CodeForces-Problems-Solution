const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let t;
const inputs = [];

rl.on("line", (line) => {
  if (t === undefined) {
    t = parseInt(line.trim());
  } else {
    inputs.push(parseInt(line.trim()));
    if (inputs.length === t) {
      rl.close();
    }
  }
});

// main solution of the problem
const solution = (n) => {
  return Math.floor(n / 15) * 3 + Math.min(n % 15, 2) + 1;
};

rl.on("close", () => {
  for (let n of inputs) {
    console.log(solution(n));
  }
  process.exit(0);
});
