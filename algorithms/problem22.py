'''
Matrix times Vector
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
Example
Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10] 
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10
'''

def matrix_times_vector(matrix, vector):
    # Get the number of rows and columns of the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Check if matrix and vector can be multiplied (cols of matrix must match length of vector)
    if cols != len(vector):
        return -1  # Return -1 if they cannot be multiplied
    
    # Initialize the result vector
    result = []
    
    # Perform matrix-vector multiplication
    for row in matrix:
        # Compute the dot product of the row and the vector
        dot_product = sum(row[i] * vector[i] for i in range(cols))
        result.append(dot_product)
    
    return result

# Example usage
a = [[1, 2], [2, 4]]
b = [1, 2]

output = matrix_times_vector(a, b)
print(output)  # Output: [5, 10]
