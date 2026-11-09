const constant = (a: number[]): number => { const x = a[0]; return 1; };  // O(1)

function logarithmic(n: number): number {  // O(log n)
  let steps = 0;
  while (n > 1) { n = Math.floor(n / 2); steps++; }
  return steps;
}

function linear(n: number): number {  // O(n)
  let steps = 0;
  for (let i = 0; i < n; i++) steps++;
  return steps;
}

function linearithmic(n: number): number {  // O(n log n)
  let steps = 0;
  for (let i = 0; i < n; i++)
    for (let m = n; m > 1; m = Math.floor(m / 2)) steps++;
  return steps;
}

function quadratic(n: number): number { // O(n^2)
  let steps = 0;
  for (let i = 0; i < n; i++)
    for (let j = 0; j < n; j++) steps++;
  return steps;
}

function exponential(n: number): number {  // O(2^n)
  if (n === 0) return 1;
  return exponential(n - 1) + exponential(n - 1);
}

function factorialTime(n: number): number {  // O(n!)
  if (n === 0) return 1;
  let total = 0;
  for (let i = 0; i < n; i++) total += factorialTime(n - 1);
  return total;
}

// ---- space ----
const copySpace = (n: number): number => new Array(n).fill(0).length;  // O(n)
function gridSpace(n: number): number { // O(n^2)
  let cells = 0;
  for (let i = 0; i < n; i++) cells += new Array(n).fill(0).length;
  return cells;
}
const depth = (n: number): number => (n === 0 ? 1 : 1 + depth(n - 1));  // O(n) stack

console.log("O(1)       ", constant([5, 6, 7]));
console.log("O(log n)   ", logarithmic(16));
console.log("O(n)       ", linear(16));
console.log("O(n log n) ", linearithmic(16));
console.log("O(n^2)     ", quadratic(16));
console.log("O(2^n)     ", exponential(10));
console.log("O(n!)      ", factorialTime(5));
console.log("space O(n) copy       ", copySpace(16));
console.log("space O(n^2) grid     ", gridSpace(16));
console.log("space O(n) recursion  ", depth(15));
