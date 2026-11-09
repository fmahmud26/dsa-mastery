def a(arr):                    # one loop                      -> O(n)
    total = 0
    for x in arr:
        total += x
    return total

def b(arr):                    # two loops, one after the other -> O(n + n) = O(n)
    total = 0
    for x in arr:
        total += x
    for x in arr:
        total -= x
    return total

def c(arr):                    # loop inside a loop             -> O(n * n) = O(n^2)
    pairs = 0
    for x in arr:
        for y in arr:
            pairs += 1
    return pairs

def d(arr):                    # constant inner loop            -> O(10n) = O(n)
    steps = 0
    for x in arr:
        for _ in range(10):
            steps += 1
    return steps

def e(n):                      # doubling until n               -> O(log n)
    i, steps = 1, 0
    while i < n:
        i *= 2
        steps += 1
    return steps

def f(a_list, b_list):         # two different inputs           -> O(a * b)
    steps = 0
    for x in a_list:
        for y in b_list:
            steps += 1
    return steps

print(a([1, 2, 3]), b([1, 2, 3]), c([1, 2, 3]), d([1, 2, 3]), e(16), f([1, 2], [1, 2, 3]))
