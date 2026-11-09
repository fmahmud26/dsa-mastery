package main

import "fmt"

func constant(a []int) int { _ = a[0]; return 1 } // O(1)

func logarithmic(n int) int { // O(log n)
	steps := 0
	for n > 1 { n /= 2; steps++ }
	return steps
}

func linear(n int) int { // O(n)
	steps := 0
	for i := 0; i < n; i++ { steps++ }
	return steps
}

func linearithmic(n int) int { // O(n log n)
	steps := 0
	for i := 0; i < n; i++ {
		for m := n; m > 1; m /= 2 { steps++ }
	}
	return steps
}

func quadratic(n int) int { // O(n^2)
	steps := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ { steps++ }
	}
	return steps
}

func exponential(n int) int { // O(2^n)
	if n == 0 { return 1 }
	return exponential(n-1) + exponential(n-1)
}

func factorialTime(n int) int { // O(n!)
	if n == 0 { return 1 }
	total := 0
	for i := 0; i < n; i++ { total += factorialTime(n - 1) }
	return total
}

// ---- space ----
func copySpace(n int) int { return len(make([]int, n)) } // O(n)
func gridSpace(n int) int { // O(n^2)
	total := 0
	for i := 0; i < n; i++ { total += len(make([]int, n)) }
	return total
}
func depth(n int) int { // O(n) stack
	if n == 0 { return 1 }
	return 1 + depth(n-1)
}

func main() {
	fmt.Println("O(1)       ", constant([]int{5, 6, 7}))
	fmt.Println("O(log n)   ", logarithmic(16))
	fmt.Println("O(n)       ", linear(16))
	fmt.Println("O(n log n) ", linearithmic(16))
	fmt.Println("O(n^2)     ", quadratic(16))
	fmt.Println("O(2^n)     ", exponential(10))
	fmt.Println("O(n!)      ", factorialTime(5))
	fmt.Println("space O(n) copy       ", copySpace(16))
	fmt.Println("space O(n^2) grid     ", gridSpace(16))
	fmt.Println("space O(n) recursion  ", depth(15))
}
