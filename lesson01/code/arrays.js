const arr = [10, 20, 30, 40, 50];

// 1. Access by index: O(1)
console.log(arr[3]);                 // 40

// 2. Linear search: O(n)
function linearSearch(a, target) {
  for (let i = 0; i < a.length; i++) {
    if (a[i] === target) return i;
  }
  return -1;
}
console.log(linearSearch(arr, 40));  // 3

// 3. Insert 25 at index 2: O(n)
arr.splice(2, 0, 25);
console.log(arr);                    // [10, 20, 25, 30, 40, 50]

// 4. Delete the element at index 2: O(n)
arr.splice(2, 1);
console.log(arr);                    // [10, 20, 30, 40, 50]

// 5. Append at the end: O(1) amortized
arr.push(60);
console.log(arr);                    // [10, 20, 30, 40, 50, 60]
