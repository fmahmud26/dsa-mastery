def constant(a):                 # O(1): one step, whatever the size
    _ = a[0]
    return 1

def logarithmic(n):              # O(log n): halve until 1
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps

def linear(n):                   # O(n): touch each item once
    steps = 0
    for _ in range(n):
        steps += 1
    return steps

def linearithmic(n):             # O(n log n): n items, each halved log n times
    steps = 0
    for _ in range(n):
        m = n
        while m > 1:
            m //= 2
            steps += 1
    return steps

def quadratic(n):                # O(n^2): every pair
    steps = 0
    for _ in range(n):
        for _ in range(n):
            steps += 1
    return steps

def exponential(n):              # O(2^n): each item is in or out
    if n == 0:
        return 1
    return exponential(n - 1) + exponential(n - 1)

def factorial_time(n):           # O(n!): every ordering
    if n == 0:
        return 1
    return sum(factorial_time(n - 1) for _ in range(n))

# ---- space ----
def copy_space(n):               # O(n) extra memory
    return len(list(range(n)))

def grid_space(n):               # O(n^2) extra memory
    return sum(len([0] * n) for _ in range(n))

def depth(n):                    # O(n) call stack
    return 1 if n == 0 else 1 + depth(n - 1)

print("O(1)      ", constant([5, 6, 7]))
print("O(log n)  ", logarithmic(16))
print("O(n)      ", linear(16))
print("O(n log n)", linearithmic(16))
print("O(n^2)    ", quadratic(16))
print("O(2^n)    ", exponential(10))
print("O(n!)     ", factorial_time(5))
print("space O(n) copy      ", copy_space(16))
print("space O(n^2) grid    ", grid_space(16))
print("space O(n) recursion ", depth(15))
