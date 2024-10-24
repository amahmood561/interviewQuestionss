'''

This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.

'''


import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.is_expanded = False  # Indicates if the children have been generated

    def expand(self):
        if not self.is_expanded:
            # Create left and right children on-demand
            self.left = TreeNode(random.randint(1, 100))  # Assign random values to make the tree look different
            self.right = TreeNode(random.randint(1, 100))
            self.is_expanded = True

def generate():
    # Return a new root node without expanding it
    return TreeNode(random.randint(1, 100))

def print_tree(node, depth=0):
    if node is None:
        return
    # Expand the node before printing to simulate lazy generation
    node.expand()
    
    # Preorder traversal for printing the tree
    print(" " * depth * 2 + str(node.value))
    print_tree(node.left, depth + 1)
    print_tree(node.right, depth + 1)

# Example usage
root = generate()  # O(1) to generate root
print("Tree (partial expansion):")
print_tree(root)   # Expands nodes lazily as we access them
'''

### Explanation:

1. **`TreeNode` class**:
   - Each node holds a value and two child references (`left` and `right`), but the children are initially `None`.
   - The `expand()` method generates the left and right children only when the node is first accessed.

2. **`generate()` function**:
   - This function creates a root node with a random value but does not expand any children yet. It runs in \( O(1) \) since no actual tree structure is being created at this point.

3. **Lazy expansion**:
   - The `expand()` method is called when you need to access the children of a node. This ensures that tree nodes are generated only when needed, allowing the tree to be unbounded but finite.

4. **Print tree**:
   - The `print_tree()` function expands each node lazily during a pre-order traversal, simulating the dynamic growth of the tree.

### Key Points:

- **Time Complexity**: The initial call to `generate()` runs in \( O(1) \), as it only creates the root node. Nodes are generated on-demand as they are accessed, meaning that we only incur the cost of generating nodes when needed.
- **Space Complexity**: Space usage grows only as the tree is expanded. If you never access certain parts of the tree, they remain unallocated.

This approach ensures that the tree can be arbitrarily large but finite, with lazy node creation allowing it to be generated in \( O(1) \) time.
'''