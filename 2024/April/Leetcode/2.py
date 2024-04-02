"""
2. Add Two Numbers

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
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def add_two_numbers(self, l1 : ListNode, l2 : ListNode) -> ListNode:

        pass
    
    def display(self, l1, l2):
        l1_current = l1
        print("First Linked List: ")
        while l1_current:
            print(l1_current.val, end=" -> ")
            l1_current = l1_current.next
        print("None")

        l2_current = l2
        print("Second Linked List: ")
        while l2_current:
            print(l2_current.val, end=" -> ")
            l2_current = l2_current.next
        print("None")

solution = Solution()

l1_head = ListNode(2)
l1_node2 = ListNode(4)
l1_node3 = ListNode(3)

l1_head.next = l1_node2
l1_node2.next = l1_node3

l2_head = ListNode(5)
l2_node2 = ListNode(6)
l2_node3 = ListNode(4)

l2_head.next = l2_node2
l2_node2.next = l2_node3

solution.display(l1_head, l2_head)