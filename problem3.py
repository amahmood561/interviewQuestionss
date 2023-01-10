
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self, root=None):
        self.root = root
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104



solution:

The Tree class has an __init__ method that takes an optional parameter root, which is used to initialize the root of the tree. The class also has a method isSameTree which takes two TreeNode objects, p and q, as input and returns a Boolean value indicating whether the two trees are the same or not. The method is similar to the one I showed you earlier, but with self argument added to it.

You can create instances of the Tree class and call the isSameTree method on them, like this:


tree1 = Tree(TreeNode(1, TreeNode(2), TreeNode(3)))
tree2 = Tree(TreeNode(1, TreeNode(2), TreeNode(3)))
print(tree1.isSameTree(tree1.root, tree2.root))  # True
This way you can have a class level tree and you can have multiple trees with same behaviour and you can keep the context of each tree.


'''