'''
Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.

'''

class TreeNode:
    def __init__(self, value=0, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def inorder_successor(node):
    # Case 1: Node has a right child
    if node.right:
        # Find the leftmost node in the right subtree
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor
    
    # Case 2: No right child, move up to find the successor
    successor = node.parent
    while successor and node == successor.right:
        node = successor
        successor = successor.parent
    
    return successor


# Step 2: Create the tree nodes
root = TreeNode(10)
node5 = TreeNode(5, parent=root)
node30 = TreeNode(30, parent=root)
node22 = TreeNode(22, parent=node30)
node35 = TreeNode(35, parent=node30)

# Connect the nodes to form the tree structure
root.left = node5
root.right = node30
node30.left = node22
node30.right = node35

# Step 3: Find the inorder successor of node 22
successor = inorder_successor(node22)

# Step 4: Print the result
if successor:
    print(f"The inorder successor of {node22.value} is {successor.value}")
else: