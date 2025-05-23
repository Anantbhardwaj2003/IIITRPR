# Write a function to check the distinct ways to climb a staircase with n steps, where you can take 1 or 2 steps at a time.
# The function should return the number of distinct ways to reach the top of the staircase.

def climb_stairs(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    # Initialize the first two steps
    first = 1
    second = 2

    # Calculate the number of ways to reach each step
    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second

c1=climb_stairs(5)
print(c1)  # Output: 8

