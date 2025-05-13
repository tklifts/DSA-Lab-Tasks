def rotate_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix (flip over the diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

# -------------------------------
# Test the implementation
# -------------------------------

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Sample input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)

rotate_matrix(matrix)

print("\nMatrix after 90° Clockwise Rotation:")
print_matrix(matrix)
