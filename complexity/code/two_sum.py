# Problem: find two numbers in `nums` that add up to `target`.

def two_sum_brute(nums, target):          # Time O(n^2), Space O(1)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_hash(nums, target):           # Time O(n), Space O(n)
    seen = {}                             # value -> index (the extra memory)
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        seen[x] = i
    return None

print(two_sum_brute([3, 8, 2, 5], 10))    # (1, 2)
print(two_sum_hash([3, 8, 2, 5], 10))     # (1, 2)
