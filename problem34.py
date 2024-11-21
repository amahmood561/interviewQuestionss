'''This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

'''

def word_in_matrix(matrix, target):
    # Check rows for the target word
    for row in matrix:
        if target in ''.join(row):
            return True

    # Check columns for the target word
    for col in zip(*matrix):  # Transpose the matrix
        if target in ''.join(col):
            return True

    return False


# Test cases
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]

# Example tests
print(word_in_matrix(matrix, "FOAM"))  # Should return True
print(word_in_matrix(matrix, "MASS"))  # Should return True
print(word_in_matrix(matrix, "ABCD"))  # Should return False
