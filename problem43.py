'''
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers

'''


def max_product_of_three(nums):
    # Sort the array
    nums.sort()
    
    # Compute the two possible largest products
    product1 = nums[-1] * nums[-2] * nums[-3]  # Largest three numbers
    product2 = nums[0] * nums[1] * nums[-1]    # Two smallest and the largest number
    
    # Return the maximum of the two
    return max(product1, product2)

# Example usage
nums = [-10, -10, 5, 2]
print(max_product_of_three(nums))  # Output: 500
