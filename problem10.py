
'''
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].

One way to implement an algorithm to print the nodes of a binary tree in boustrophedon order is to use a modified version of a breadth-first search (BFS) traversal.

Here's a possible algorithm in Python:
'''

def boustrophedon_order(root):
    result = []
    if not root:
        return result
    
    # Create a queue for BFS and add the root node
    queue = []
    queue.append(root)
    
    # Create a flag to keep track of the direction
    left_to_right = True
    
    # Run while there are nodes in the queue
    while queue:
        # Get the size of the current level
        level_size = len(queue)
        
        # Create a stack for storing the current level nodes
        level_stack = []
        
        # Traverse the current level
        for i in range(level_size):
            # Dequeue a node from the queue
            current_node = queue.pop(0)
            
            # Add the current node to the stack
            level_stack.append(current_node.val)
            
            # Enqueue the left and right children of the current node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        # Append the current level nodes to the result list
        if left_to_right:
            result.extend(level_stack)
        else:
            result.extend(level_stack[::-1])
        
        # Flip the direction flag
        left_to_right = not left_to_right
    
    return result
'''
This algorithm uses a queue to traverse the tree level by level, and a stack to store the nodes of the 
current level. The algorithm also uses a flag to keep track of the direction (left to right or right to left) 
in which the nodes of the current level should be appended to the result list. 
The algorithm traverses the tree in a breadth-first manner and for each level, it first 
traverses from left to right and next from right to left this is how the boustrophedon traversal works.
'''