'''

        1
       / \
      2   3
     / \   \
    4   5   6

Level 0: sum = 1
Level 1: sum = 2 + 3 = 5
Level 2: sum = 4 + 5 + 6 = 15
The function will return 0 because the sum at level 0 is the smallest.
Given a binary tree, return the level of the tree with minimum sum.

This approach ensures that each node is processed once, making the time complexity O(n), where n is the number of nodes in the tree.
'''



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_sum_level(root):
    if not root:
        return -1  # return -1 if the tree is empty

    queue = deque([root])
    min_sum = float('inf')
    min_level = 0
    level = 0

    while queue:
        level_sum = 0
        num_nodes = len(queue)

        for _ in range(num_nodes):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Check if the current level has the smallest sum
        if level_sum < min_sum:
            min_sum = level_sum
            min_level = level

        level += 1

    return min_level



# Creating the binary tree
root = TreeNode(1)                    # Root node with value 1
root.left = TreeNode(2)                # Left child of root
root.right = TreeNode(3)               # Right child of root
root.left.left = TreeNode(4)           # Left child of node 2
root.left.right = TreeNode(5)          # Right child of node 2
root.right.right = TreeNode(6)         # Right child of node 3

# Call the function to find the level with the minimum sum
min_level = min_sum_level(root)
print("Level with minimum sum is:", min_level)
