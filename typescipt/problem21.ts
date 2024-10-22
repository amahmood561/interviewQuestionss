/*Q: arr is a 2 dimension array having same rows and columns (2x2, 3x3 so on) write a method ArrFlip(arr) that transform rows into column but first row should be the last column and last row become first column. 
eg: [[8, 2, 3],
 [1, 5, 6],
 [6, 7, 0]]

to: [[6, 1, 8],
 [7, 5, 2],
 [0, 6, 3]]

*/
function ArrFlip(arr: number[][]): number[][] {
    const n = arr.length;  // Size of the square matrix (number of rows/columns)
    
    // Step 1: Create an empty matrix for the transposed and flipped result
    const result: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    
    // Step 2: Perform the transpose and reverse rows in one go
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            // Transpose and reverse: The element at arr[i][j] moves to result[j][n - 1 - i]
            result[j][n - 1 - i] = arr[i][j];
        }
    }
    
    return result;
}

// Example usage
const arr: number[][] = [
    [8, 2, 3],
    [1, 5, 6],
    [6, 7, 0]
];

const flippedArr = ArrFlip(arr);

// Print the result
for (let row of flippedArr) {
    console.log(row);
}
