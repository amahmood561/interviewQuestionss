'''
Given two non-empty binary trees s and t, 
check whether tree t has exactly the same structure and node values
 with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
'''

from dataclasses import dataclass
from typing import Optional

@dataclass
class TreeNode:
    """Class for a binary tree node."""
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

def is_identical(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    """
    Checks if two binary trees are identical.
    
    Args:
    s (TreeNode): Root of the first tree.
    t (TreeNode): Root of the second tree.
    
    Returns:
    bool: True if trees are identical, False otherwise.
    """
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return is_identical(s.left, t.left) and is_identical(s.right, t.right)

def is_subtree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    """
    Determines if tree t is a subtree of tree s.
    
    Args:
    s (TreeNode): Root of the main tree.
    t (TreeNode): Root of the subtree to check.
    
    Returns:
    bool: True if t is a subtree of s, False otherwise.
    """
    if not t:
        return True  # An empty tree is always a subtree
    if not s:
        return False  # Non-empty t can't be a subtree of an empty s
    
    if is_identical(s, t):
        return True
    
    # Recursively check left and right subtrees of s
    return is_subtree(s.left, t) or is_subtree(s.right, t)

# Example Usage
if __name__ == "__main__":
    # Construct tree s
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    
    # Construct tree t
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    
    # Check if t is a subtree of s
    result = is_subtree(s, t)
    print("Is t a subtree of s?", result)  # Output: True
