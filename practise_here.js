function longestSubarray(arr) {
  let left = 0;
  let count = new Map();
  let maxLength = 0;

  for (let right = 0; right < arr.length; right++) {
    count.set(arr[right], (count.get(arr[right]) || 0) + 1);

    while (
      count.size > 2 ||
      Math.max(...count.keys()) - Math.min(...count.keys()) > 1
    ) {
      count.set(arr[left], count.get(arr[left]) - 1);
      if (count.get(arr[left]) === 0) {
        count.delete(arr[left]);
      }
      left++;
    }

    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}

// console.log(longestSubarray([1, 2, 1, 2, 3]));
// console.log(longestSubarray([3, 3, 2, 2]));
// console.log(longestSubarray([1, 1, 1, 3, 3]));
