'''
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.



'''


def reverse(lst, i, j):
    """Reverses the list from index i to j."""
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

def find_max_index(lst, n):
    """Finds the index of the maximum element in lst[0:n]."""
    max_idx = 0
    for i in range(1, n):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(lst):
    """Sorts the list using reverse(lst, i, j) method."""
    n = len(lst)
    
    # Go through the list and move the maximum elements to their correct position
    for curr_size in range(n, 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = find_max_index(lst, curr_size)
        
        if max_idx != curr_size - 1:
            # Bring the maximum element to the front if it's not already there
            if max_idx > 0:
                reverse(lst, 0, max_idx)
            
            # Now move it to the correct position (end of the unsorted portion)
            reverse(lst, 0, curr_size - 1)

# Example usage:
lst = [3, 6, 2, 7, 5, 4, 1]
pancake_sort(lst)
print(lst)  # Output will be a sorted list
