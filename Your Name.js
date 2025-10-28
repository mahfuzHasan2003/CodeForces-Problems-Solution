const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split(/\s+/);

let index = 0;
const q = Number(input[index++]);

for (let i = 0; i < q; i++) {
   const n = Number(input[index++]);
   const s = input[index++].split("").sort();
   const t = input[index++].split("").sort();

   if (s.length !== t.length || s.length !== n || t.length !== n) console.log("NO");
   else console.log(s.every((val, i) => t[i] === val) ? "YES" : "NO");
}
