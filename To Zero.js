const readline = require("readline");

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

// Function to calculate minimum operations
const minimumOperations = (n, k) => {
   let count = 0;
   if (n % 2 !== 0) {
      n -= k;
      count++;
   }
   let maxEvenK = k % 2 === 0 ? k : k - 1;
   count += Math.floor(n / maxEvenK);
   n %= maxEvenK;
   while (n > 0) {
      n -= maxEvenK;
      count++;
   }

   return count;
}

// Reading input and processing test cases
let input = [];
rl.on("line", (line) => {
   input.push(line);
}).on("close", () => {
   const t = parseInt(input[0]); // Number of test cases
   let results = [];

   for (let i = 1; i <= t; i++) {
      let [n, k] = input[i].split(" ").map(Number);
      results.push(minimumOperations(n, k));
   }

   console.log(results.join("\n"));
   process.exit(0);
});




// console.log(minimumOperations(6, 5));
// console.log(minimumOperations(39, 7));
// console.log(minimumOperations(1000000000, 3));
// console.log(minimumOperations(999999999, 3));
// console.log(minimumOperations(999967802, 3));