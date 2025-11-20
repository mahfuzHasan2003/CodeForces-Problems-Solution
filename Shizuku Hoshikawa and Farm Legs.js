'use strict';

const fs = require('fs');

function main() {
   const data = fs.readFileSync(0, 'utf8').trim().split(/\s+/);
   if (data.length === 0 || data[0] === '') return;
   let idx = 0;
   const t = Number(data[idx++]);

   const outputs = [];
   for (let tc = 0; tc < t; tc++) {
      const n = Number(data[idx++]);
      outputs.push(String(solution(n)));
   }

   console.log(outputs.join('\n'));
}

function solution(n) {
   return n % 2 !== 0 ? 0 : Math.floor(n / 4) + 1;
}

main();
