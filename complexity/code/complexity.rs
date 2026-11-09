fn constant(a: &[i32]) -> u64 { let _ = a[0]; 1 } // O(1)

fn logarithmic(mut n: u64) -> u64 { // O(log n)
    let mut steps = 0;
    while n > 1 { n /= 2; steps += 1; }
    steps
}

fn linear(n: u64) -> u64 { // O(n)
    let mut steps = 0;
    for _ in 0..n { steps += 1; }
    steps
}

fn linearithmic(n: u64) -> u64 { // O(n log n)
    let mut steps = 0;
    for _ in 0..n {
        let mut m = n;
        while m > 1 { m /= 2; steps += 1; }
    }
    steps
}

fn quadratic(n: u64) -> u64 { // O(n^2)
    let mut steps = 0;
    for _ in 0..n { for _ in 0..n { steps += 1; } }
    steps
}

fn exponential(n: u32) -> u64 { // O(2^n)
    if n == 0 { return 1; }
    exponential(n - 1) + exponential(n - 1)
}

fn factorial_time(n: u32) -> u64 { // O(n!)
    if n == 0 { return 1; }
    (0..n).map(|_| factorial_time(n - 1)).sum()
}

// ---- space ----
fn copy_space(n: usize) -> usize { vec![0; n].len() } // O(n)
fn grid_space(n: usize) -> usize { // O(n^2)
    (0..n).map(|_| vec![0; n].len()).sum()
}
fn depth(n: u32) -> u32 { if n == 0 { 1 } else { 1 + depth(n - 1) } } // O(n) stack

fn main() {
    println!("O(1)        {}", constant(&[5, 6, 7]));
    println!("O(log n)    {}", logarithmic(16));
    println!("O(n)        {}", linear(16));
    println!("O(n log n)  {}", linearithmic(16));
    println!("O(n^2)      {}", quadratic(16));
    println!("O(2^n)      {}", exponential(10));
    println!("O(n!)       {}", factorial_time(5));
    println!("space O(n) copy        {}", copy_space(16));
    println!("space O(n^2) grid      {}", grid_space(16));
    println!("space O(n) recursion   {}", depth(15));
}
