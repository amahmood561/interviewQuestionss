class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def convert_to_full_binary_tree(root):
    """
    Converts a binary tree to a full binary tree by removing nodes with only one child.

    :param root: TreeNode - The root of the binary tree.
    :return: TreeNode - The root of the full binary tree.
    """
    if root is None:
        return None

    # Recursively convert left and right subtrees
    root.left = convert_to_full_binary_tree(root.left)
    root.right = convert_to_full_binary_tree(root.right)

    # If the node has only one child, return that child
    if root.left is None and root.right is not None:
        return root.right
    if root.right is None and root.left is not None:
        return root.left

    # If the node has two children or no children, return the node itself
    return root

def build_sample_tree():
    """
    Builds the sample tree provided in the problem statement.

             0
          /     \
        1         2
      /            \
    3                 4
      \             /   \
        5          6     7

    :return: TreeNode - The root of the sample binary tree.
    """
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    return root

def print_inorder(root):
    """
    Prints the in-order traversal of the binary tree.

    :param root: TreeNode - The root of the binary tree.
    """
    if root is None:
        return
    print_inorder(root.left)
    print(root.value, end=' ')
    print_inorder(root.right)

if __name__ == "__main__":
    # Build the sample tree
    root = build_sample_tree()
    print("Original Tree In-order Traversal:")
    print_inorder(root)
    print("\n")

    # Convert to full binary tree
    full_root = convert_to_full_binary_tree(root)
    print("Full Binary Tree In-order Traversal:")
    print_inorder(full_root)
    print("\n")
