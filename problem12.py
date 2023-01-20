'''
facebook 

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

'''


def check(arr):
    modify = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            modify += 1
            if modify > 1:
                return False
            if i-2 >= 0 and arr[i] < arr[i-2]:
                arr[i] = arr[i-1]
    return True

'''
This function iterates through the array, starting at index 1. It compares each element with the previous one. 
If the current element is less than the previous one, it increments a counter called "modify". If "modify" is greater than 1, 
the function returns False, as we can't modify more than 1 element to make the array non-decreasing. If "modify" is 1 and the current element is 
less than the element before the previous one, it replaces the current element with the previous one.

The function returns True if it finishes iterating without returning False, indicating that the array could become non-decreasing by modifying at most 1 element.
'''