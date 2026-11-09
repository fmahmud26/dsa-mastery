package main

import "fmt"

func linearSearch(a []int, target int) int {
	for i := range a {
		if a[i] == target {
			return i
		}
	}
	return -1
}

func main() {
	arr := []int{10, 20, 30, 40, 50}

	// 1. Access by index: O(1)
	fmt.Println(arr[3]) // 40

	// 2. Linear search: O(n)
	fmt.Println(linearSearch(arr, 40)) // 3

	// 3. Insert 25 at index 2: O(n)
	arr = append(arr[:2], append([]int{25}, arr[2:]...)...)
	fmt.Println(arr) // [10 20 25 30 40 50]

	// 4. Delete the element at index 2: O(n)
	arr = append(arr[:2], arr[3:]...)
	fmt.Println(arr) // [10 20 30 40 50]

	// 5. Append at the end: O(1) amortized
	arr = append(arr, 60)
	fmt.Println(arr) // [10 20 30 40 50 60]
}
