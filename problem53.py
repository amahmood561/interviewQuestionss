
'''
Given an array of integers out of order, determine the bounds 
of the smallest window that must be sorted in order for the entire array to be sorted. 
For example, given [3, 7, 5, 6, 9], you should return (1, 3).

'''
def find_unsorted_window(arr):
    n = len(arr)
    start, end = 0, n - 1

    # Step 1: Find the first element out of order from the start
    while start < n - 1 and arr[start] <= arr[start + 1]:
        start += 1
    if start == n - 1:
        return (0, 0)  # Already sorted

    # Step 2: Find the first element out of order from the end
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    # Step 3: Find min and max in the subarray
    window_min = min(arr[start:end+1])
    window_max = max(arr[start:end+1])

    # Step 4: Expand to the left
    while start > 0 and arr[start - 1] > window_min:
        start -= 1

    # Step 5: Expand to the right
    while end < n - 1 and arr[end + 1] < window_max:
        end += 1

    return (start, end)

# Example
print(find_unsorted_window([3, 7, 5, 6, 9]))  # Output: (1, 3)
