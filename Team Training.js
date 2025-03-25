const readline = require("readline");

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

let input = [];
rl.on("line", (line) => {
   input.push(line.trim());
}).on("close", () => {
   processTestCases(input);
});

function programSolution(x, skills = []) {
   skills.sort((a, b) => b - a);
   let teamCount = 0;
   let teamSize = 0;
   for (let i = 0; i < skills.length; i++) {
      teamSize++;
      if (teamSize * skills[i] >= x) {
         teamCount++;
         teamSize = 0;
      }
   }
   return teamCount;
}

// console.log(programSolution(4, [4, 5, 3, 3, 2, 6, 3, 2]));


function processTestCases(input) {
   let index = 0;
   const t = parseInt(input[index++]);
   let results = [];
   for (let i = 0; i < t; i++) {
      let [n, x] = input[index++].split(" ").map(Number);
      let skills = input[index++].split(" ").map(Number);
      let maxTeams = programSolution(x, skills);
      results.push(maxTeams);
   }
   console.log(results.join("\n"));
}
