'''

To convert a sorted array into a height-balanced binary search tree (BST), you can use the following approach:

Take the middle element of the array as the root of the BST.
Recursively do the same for the left half and right half of the array:
The middle element of the left half becomes the left child of the root.
The middle element of the right half becomes the right child of the root.
Repeat the process until you process all elements in the array.
Here's the code to achieve this:
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    # Base case
    if not nums:
        return None

    # Find the middle of the array
    mid = len(nums) // 2

    # Create a root node with the middle element
    root = TreeNode(nums[mid])

    # Recursively build the left and right subtrees
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

# Test
nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
