'''
Salesforce.

Given an array of integers, find the maximum XOR of any two elements.
'''

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums):
        # Initialize Trie
        root = TrieNode()
        
        # Function to insert number into Trie
        def insert(num):
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # Function to find the max XOR for a given number
        def findMaxXOR(num):
            node = root
            max_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled_bit = 1 - bit
                if toggled_bit in node.children:
                    max_xor = (max_xor << 1) | 1
                    node = node.children[toggled_bit]
                else:
                    max_xor = (max_xor << 1) | 0
                    node = node.children[bit]
            return max_xor

        # Insert all numbers into Trie
        for num in nums:
            insert(num)

        # Compute the maximum XOR
        max_result = 0
        for num in nums:
            max_result = max(max_result, findMaxXOR(num))

        return max_result

# Example usage
solution = Solution()
nums = [3, 10, 5, 25, 2, 8]
print("The maximum XOR is:", solution.findMaximumXOR(nums))
