'''Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluate_tree(root):
    # Base case: if the node is a leaf (integer), return its value
    if root.left is None and root.right is None:
        return root.value

    # Recursive case: evaluate the left and right subtrees
    left_value = evaluate_tree(root.left)
    right_value = evaluate_tree(root.right)

    # Apply the operator at the root
    if root.value == '+':
        return left_value + right_value
    elif root.value == '-':
        return left_value - right_value
    elif root.value == '*':
        return left_value * right_value
    elif root.value == '/':
        return left_value / right_value
    else:
        raise ValueError("Unknown operator: " + str(root.value))

# Example usage:
root = TreeNode('*',
                TreeNode('+', TreeNode(3), TreeNode(2)),
                TreeNode('+', TreeNode(4), TreeNode(5)))

result = evaluate_tree(root)
print(result)  # Output should be 45
'''
Explanation:
TreeNode class: This class represents each node in the tree. value is either an integer (for leaves) or an operator (for internal nodes). left and right are the left and right children of the node, respectively.

evaluate_tree function:

If the node is a leaf (has no children), it directly returns its integer value.
If the node is an operator, it recursively evaluates the left and right subtrees.
Once the left and right values are obtained, it applies the operator and returns the result.


'''