'''
Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time
'''


def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == x:
            return True  # Element found
        elif arr[mid] < x:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half
    
    return False  # Element not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]
x = 7
print(binary_search(arr, x))  # Output: True

x = 6
print(binary_search(arr, x))  # Output: False
