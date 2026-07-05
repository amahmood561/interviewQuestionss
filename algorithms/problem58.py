'''
Suppose you are given two lists of n points, 
one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ...,
 qn on the line y = 1. Imagine a set of n line segments 
 connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

'''
def count_intersections(p, q):
    n = len(p)
    # Create a list of pairs (p[i], q[i])
    segments = [(p[i], q[i]) for i in range(n)]
    # Sort segments by their starting points
    segments.sort()
    # Count intersections
    intersections = 0
    for i in range(n):
        for j in range(i + 1, n):
            if segments[i][1] > segments[j][1]:  # If they intersect
                intersections += 1
    return intersections

# Example usage:
p = [1, 2, 3]
q = [3, 2, 1]
print(count_intersections(p, q))  # Output: 3
