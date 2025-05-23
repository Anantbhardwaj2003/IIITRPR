# Write a function that takes a two word strings and returns the minimum number of operations required to convert one string into the other.
# The allowed operations are insertion, deletion, or substitution of a single character.

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D array to store the distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Deletion cost
    for j in range(n + 1):
        dp[0][j] = j  # Insertion cost

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,     # Deletion
                               dp[i][j - 1] + 1,     # Insertion
                               dp[i - 1][j - 1] + 1) # Substitution

    return dp[m][n]

c1=edit_distance("kitten", "sitting")
print(c1)  # Output: 3 (kitten -> sitten -> sittin -> sitting)