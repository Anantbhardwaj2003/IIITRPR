# Write a function that takes a matrix of size m*n and sets the entire row and column to zero if an element is zero.
# The function should modify the matrix in place and return nothing.

def set_matrix_zeroes(matrix):
    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    # First pass: find all the rows and columns that need to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Second pass: set the rows to zero
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Third pass: set the columns to zero
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0
    return matrix

c1=set_matrix_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
print(c1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]