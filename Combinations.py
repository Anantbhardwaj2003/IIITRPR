# Write a function that takes two integers n and k, and returns all possible combinations of k numbers chosen from the range 1 to n (inclusive).
def combine(n, k):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(1, [])
    return result

c1 = combine(4, 2)
print(c1)  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]