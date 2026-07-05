'''
Given an array of a million integers between 
zero and a billion, out of order, how can you efficiently sort it? 
Assume that you cannot store an array of a billion elements in memory.
'''

def bucket_sort(arr):
    # Define the number of buckets
    num_buckets = 1000  # You can adjust this for optimal performance
    max_value = 10**9
    min_value = 0

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]
    bucket_range = (max_value - min_value) / num_buckets

    # Distribute array elements into buckets
    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index == num_buckets:  # Handle edge case for max value
            index -= 1
        buckets[index].append(num)

    # Sort each bucket and concatenate
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array


# Example usage
import random

# Generate a random array of a million integers between 0 and 1 billion
array = [random.randint(0, 10**9) for _ in range(10**6)]

# Sort the array
sorted_array = bucket_sort(array)

''''
2. Why This Works
Memory Efficiency: The buckets are small, and we sort them individually, so we avoid storing all data in memory at once.
Parallelizable: Bucket sorting is naturally parallelizable as each bucket can be sorted independently.



'''