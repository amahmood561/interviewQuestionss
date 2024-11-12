'''
 Facebook question 

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.

'''

class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        # Store only non-zero values with their indices
        self.data = {i: val for i, val in enumerate(arr) if val != 0}

    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

        if val != 0:
            self.data[i] = val
        elif i in self.data:
            del self.data[i]

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.data.get(i, 0)

# Example usage
arr = [0, 0, 0, 3, 0, 0, 0, 7, 0]
sparse_array = SparseArray(arr, len(arr))

# Get values
print(sparse_array.get(3))  # Output: 3
print(sparse_array.get(7))  # Output: 7
print(sparse_array.get(1))  # Output: 0 (not in sparse array)

# Set values
sparse_array.set(3, 0)      # Removes index 3 from sparse array
sparse_array.set(5, 9)      # Adds index 5 with value 9

# Get updated values
print(sparse_array.get(3))  # Output: 0 (removed)
print(sparse_array.get(5))  # Output: 9
