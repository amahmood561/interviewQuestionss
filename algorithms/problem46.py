'''
A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
'''

import heapq

def generate_regular_numbers(N):
    """
    Generates the first N regular numbers in sorted order.

    Parameters:
        N (int): The number of regular numbers to generate.

    Returns:
        list: A list of the first N regular numbers.
    """
    # Min-heap to maintain the order of regular numbers
    heap = []
    heapq.heappush(heap, 1)

    # Set to avoid duplicates
    seen = set()
    seen.add(1)

    # Result list to store the first N regular numbers
    result = []

    # Generate regular numbers
    for _ in range(N):
        smallest = heapq.heappop(heap)
        result.append(smallest)

        # Generate next regular numbers by multiplying the smallest number with 2, 3, and 5
        for factor in [2, 3, 5]:
            new_number = smallest * factor
            if new_number not in seen:
                heapq.heappush(heap, new_number)
                seen.add(new_number)

    return result

# Example usage
if __name__ == "__main__":
    N = int(input("Enter the number of regular numbers to generate: "))
    print("The first {} regular numbers are: ".format(N))
    print(generate_regular_numbers(N))