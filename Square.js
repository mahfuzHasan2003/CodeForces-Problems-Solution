const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split(/\s+/);

let index = 0;
const t = Number(input[index++]);

for (let i = 0; i < t; i++) {
   const a = Number(input[index++]);
   const b = Number(input[index++]);
   const c = Number(input[index++]);
   const d = Number(input[index++]);

   console.log(new Set([a, b, c, d]).size === 1 ? "YES" : "NO");

}
