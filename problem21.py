'''
Q: arr is a 2 dimension array having same rows and columns (2x2, 3x3 so on) write a method ArrFlip(arr) that transform rows into column but first row should be the last column and last row become first column. 
eg: [[8, 2, 3],
 [1, 5, 6],
 [6, 7, 0]]

to: [[6, 1, 8],
 [7, 5, 2],
 [0, 6, 3]]

'''
def BruteArrFlip(arr):
    n = len(arr)  # Get the number of rows (or columns, since it's a square matrix)
    
    # Step 1: Create an empty matrix for the transposed and flipped result
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # Step 2: Perform the transpose and reverse rows in one go
    for i in range(n):
        for j in range(n):
            # Transpose and reverse: The element at arr[i][j] moves to result[j][n - 1 - i]
            result[j][n - 1 - i] = arr[i][j]
    
    return result

arr = [[8, 2, 3],
       [1, 5, 6],
       [6, 7, 0]]

flipped_arr = BruteArrFlip(arr)
for row in flipped_arr:
    print(row)


def ArrFlip(arr):
    # First, transpose the array by swapping rows with columns
    transposed = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    
    # Then, reverse the rows to get the desired output
    flipped = [row[::-1] for row in transposed]
    
    return flipped

arr = [[8, 2, 3],
       [1, 5, 6],
       [6, 7, 0]]

flipped_arr = ArrFlip(arr)
for row in flipped_arr:
    print(row)
