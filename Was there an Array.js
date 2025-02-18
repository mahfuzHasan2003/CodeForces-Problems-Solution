const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", (line) => {
  input.push(line.trim());
}).on("close", () => {
  const t = parseInt(input[0], 10);
  let index = 1;

  for (let i = 0; i < t; i++) {
    const n = parseInt(input[index], 10);
    const b = input[index + 1].split(" ").map(Number);
    index += 2;

    const result = solution(n, b);
    console.log(result ? "YES" : "NO");
  }
});

function solution(n, b) {
  const strOfArray = b.join("");
  return !strOfArray.includes("101");
}
