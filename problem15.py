'''
Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters. To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their encoded binary strings.



'''

from collections import defaultdict

# Define a node structure for the tree
class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

# Function to build the Huffman Tree
def build_huffman_tree(frequency_dict):
    # Step 1: Create a list of leaf nodes for each character
    nodes = [Node(char, freq) for char, freq in frequency_dict.items()]

    # Step 2: Build the Huffman Tree without heapq
    while len(nodes) > 1:
        # Sort the nodes based on frequency (ascending order)
        nodes = sorted(nodes, key=lambda node: node.freq)
        
        # Extract the two nodes with the lowest frequency
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq, left, right)
        
        # Add the new node back to the list of nodes
        nodes.append(merged)

    # The remaining node is the root of the Huffman Tree
    return nodes[0]

# Function to generate the Huffman codes
def generate_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    
    # Base case: If it's a leaf node, assign the current code
    if node.char is not None:
        codes[node.char] = current_code
        return codes
    
    # Traverse left and right to generate codes
    if node.left:
        generate_codes(node.left, current_code + "0", codes)
    if node.right:
        generate_codes(node.right, current_code + "1", codes)
    
    return codes

# Example usage
if __name__ == "__main__":
    # Example character frequencies
    frequency_dict = {
        'a': 5,
        'c': 1,
        't': 3,
        's': 2
    }
    
    # Step 1: Build the Huffman Tree
    huffman_tree_root = build_huffman_tree(frequency_dict)
    
    # Step 2: Generate Huffman codes
    huffman_codes = generate_codes(huffman_tree_root)
    
    # Output the codes
    print("Character Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
