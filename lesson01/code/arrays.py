arr = [10, 20, 30, 40, 50]

# 1. Access by index: O(1)
print(arr[3])                 # 40

# 2. Linear search: O(n)
def linear_search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i
    return -1

print(linear_search(arr, 40)) # 3

# 3. Insert 25 at index 2: O(n)
arr.insert(2, 25)
print(arr)                    # [10, 20, 25, 30, 40, 50]

# 4. Delete the element at index 2: O(n)
arr.pop(2)
print(arr)                    # [10, 20, 30, 40, 50]

# 5. Append at the end: O(1) amortized
arr.append(60)
print(arr)                    # [10, 20, 30, 40, 50, 60]
