const readline = require("readline");

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

let t;
let testCases = [];

rl.on("line", (line) => {
   if (typeof t === "undefined") {
      t = parseInt(line.trim()); // Read number of test cases
   } else {
      testCases.push(line.trim());
      if (testCases.length % 2 === 0) {
         processTestCases();
      }
   }
});


const mainSolution = (digits = []) => {
   let count = 0;
   let date = [0, 0, 0, 1, 2, 2, 3, 5];
   for (const element of digits) {
      count++;
      if (date.includes(element)) {
         date.splice(date.indexOf(element), 1);
         if (date.length === 0) return count;
      }
   }
   return 0;
}

function processTestCases() {
   while (testCases.length) {
      let n = parseInt(testCases.shift());
      let digits = testCases.shift().split(" ").map(Number);
      console.log(mainSolution(digits));
   }
}

// console.log(mainSolution([2, 0, 1, 2, 3, 2, 5, 0, 0, 1]));
// console.log(mainSolution([2, 0, 1, 2, 3, 2, 5, 0]));
// console.log(mainSolution([2, 0, 1, 0, 3, 2, 5, 0]));
// console.log(mainSolution([2, 3, 1, 2, 3, 0, 1, 9, 2, 1, 0, 3, 5, 4, 0, 3]));
