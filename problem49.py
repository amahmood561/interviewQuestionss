'''
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].


'''

def partition_list(lst, x):
    less = []
    equal = []
    greater = []
    
    for item in lst:
        if item < x:
            less.append(item)
        elif item == x:
            equal.append(item)
        else:
            greater.append(item)
    
    return less + equal + greater

# Example usage
x = 10
lst = [9, 12, 3, 5, 14, 10, 10]
partitioned_list = partition_list(lst, x)
print(partitioned_list)
