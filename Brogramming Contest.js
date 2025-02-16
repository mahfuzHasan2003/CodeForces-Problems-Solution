const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let t,
  testCases = [],
  currentCase = 0;

rl.on("line", (line) => {
  if (typeof t === "undefined") {
    t = parseInt(line.trim());
  } else {
    testCases.push(line.trim());
    if (testCases.length === t * 2) {
      rl.close();
    }
  }
});

rl.on("close", () => {
  for (let i = 0; i < testCases.length; i += 2) {
    const n = parseInt(testCases[i]);
    const s = testCases[i + 1];
    console.log(solution(n, s));
  }
});

function solution(n, s = "") {
  let minimumMove = 0;
  let searchingFor = "1";
  for (let i = 0; i < s.length; i++) {
    if (s[i] === searchingFor) {
      minimumMove += 1;
      searchingFor = searchingFor === "1" ? "0" : "1";
    }
  }
  return minimumMove;
}

// console.log(solution(3, "001"));
