# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head=None):
        self.head = head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        current = dummy    
        carry = 0          

        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            s = x + y + carry                 

            carry = s // 10                  
            current.next = ListNode(s % 10) 
            current = current.next           

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry) 

        return dummy.next                  

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

This function takes two ListNode objects, l1 and l2, representing the two numbers in reverse order, and returns a new ListNode object representing the sum of the two numbers in reverse order.

The function first creates a dummy node and a variable carry initialized to 0. Then it iterates through the two input lists, using the while loop.

Inside the loop, it gets the value of the current digit of l1 and l2, or 0 if one of the lists is shorter, then add the digits and the carry.

Then it checks the current sum, If the sum is greater than 9 it means we have to carry over one to next number.

After the loop, it creates a new node with the last carry if it's greater than 0. Finally, the function returns the list starting from the first real node (after the dummy), which is the head of the linked list

It is a bit tricky because it's using carry and the sum is calculated in reverse order, you may have to test it for few edge cases.


The LinkedList class has an __init__ method that takes an optional parameter head, which is used to initialize the head of the linked list. The class also has a method addTwoNumbers which takes two ListNode objects, l1 and l2, as input and returns a ListNode object representing the sum of the two numbers in reverse order. The implementation of the method is same as the one I showed you earlier, but with self argument added to it.

You can create instances of the LinkedList class and call the addTwoNumbers method on them, like this:


node1 = ListNode(2)
node1.next = ListNode(4)
node1.next.next = ListNode(3)

node2 = ListNode(5)
node2.next = ListNode(6)
node2.next.next = ListNode(4)

ll = LinkedList()
result_node = ll.addTwoNumbers(node1, node2)

while(result_node):
    print(result_node.val)
    result_node = result_node.next
    
This way you can create multiple linked list and keep context of each one by just creating new instance.
'''