fn linear_search(a: &[i32], target: i32) -> Option<usize> {
    for (i, &x) in a.iter().enumerate() {
        if x == target {
            return Some(i);
        }
    }
    None
}

fn main() {
    let mut arr = vec![10, 20, 30, 40, 50];

    // 1. Access by index: O(1)
    println!("{}", arr[3]); // 40

    // 2. Linear search: O(n)
    println!("{:?}", linear_search(&arr, 40)); // Some(3)

    // 3. Insert 25 at index 2: O(n)
    arr.insert(2, 25);
    println!("{:?}", arr); // [10, 20, 25, 30, 40, 50]

    // 4. Delete the element at index 2: O(n)
    arr.remove(2);
    println!("{:?}", arr); // [10, 20, 30, 40, 50]

    // 5. Append at the end: O(1) amortized
    arr.push(60);
    println!("{:?}", arr); // [10, 20, 30, 40, 50, 60]
}
