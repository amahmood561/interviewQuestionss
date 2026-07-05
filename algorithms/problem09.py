'''
palantir problem
Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, where h is the height of the tree.
 Write a program in python to compute the in-order traversal of a binary tree using O(1) space. 

typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, where h is the height of the tree.
 Write a program in python to compute the in-order traversal of a binary tree using O(1) space. 
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.isThreaded = False


def inOrder(root):
    cur = leftmost(root)
    while cur:
        print(cur.data, end=' ')
        if cur.isThreaded:
            cur = cur.right
        else:
            cur = leftmost(cur.right)

def leftmost(root):
    while root:
        if root.left:
            root = root.left
        else:
            return root
    return None

def insert(root, data):
    newNode = Node(data)
    if root is None:
        return newNode
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def createThreaded(root):
    if root is None:
        return
    if root.left:
        createThreaded(root.left)
    if root.right:
        createThreaded(root.right)
    if root.left is None:
        root.left = prev
        root.isThreaded = True
    if prev and prev.right is None:
        prev.right = root
        prev.isThreaded = True
    prev = root

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root,90)



'''


The prev variable is declared within the createThreaded function, while it is being used in the inOrder function, In order to fix this issue, you can move the prev variable to the global scope or you can pass it as 
an argument to the createThreaded function and the inOrder function, so they share the same value.


prev = None
def inOrder(root):
    cur = leftmost(root)
    while cur:
        print(cur.data, end=' ')
        if cur.isThreaded:
            cur = cur.right
        else:
            cur = leftmost(cur.right)

def createThreaded(root):
    global prev
    if root is None:
        return
    if root.left:
        createThreaded(root.left)
    if root.right:
        createThreaded(root.right)
    if root.left is None:
        root.left = prev
        root.isThreaded = True
    if prev and prev.right is None:
        prev.right = root
        prev.isThreaded = True
    prev = root

    
It's worth noting that threaded binary trees are not widely used, it's not a common algorithm to use, and also it's not efficient with all type of data sets, this is a particular
 case where space is the critical factor, for most cases other algorithms are more efficient.

'''