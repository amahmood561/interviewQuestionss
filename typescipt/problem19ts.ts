/*
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
*/

function reverse(lst: number[], i: number, j: number): void {
    while (i < j) {
        [lst[i], lst[j]] = [lst[j], lst[i]]; // Swap elements
        i++;
        j--;
    }
}

function findMaxIndex(lst: number[], n: number): number {
    let maxIdx = 0;
    for (let i = 1; i < n; i++) {
        if (lst[i] > lst[maxIdx]) {
            maxIdx = i;
        }
    }
    return maxIdx;
}

function pancakeSort(lst: number[]): void {
    const n = lst.length;

    // Go through the list and move the maximum elements to their correct position
    for (let currSize = n; currSize > 1; currSize--) {
        // Find the index of the maximum element in the unsorted portion
        const maxIdx = findMaxIndex(lst, currSize);

        if (maxIdx !== currSize - 1) {
            // Bring the maximum element to the front if it's not already there
            if (maxIdx > 0) {
                reverse(lst, 0, maxIdx);
            }

            // Now move it to the correct position (end of the unsorted portion)
            reverse(lst, 0, currSize - 1);
        }
    }
}

// Example usage:
const lst = [3, 6, 2, 7, 5, 4, 1];
pancakeSort(lst);
console.log(lst);  // Output will be a sorted list
