"""
83. Remove Duplicates from Sorted List
Solved
Easy
Topics
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
# SEE LEETCODE SITE DESCRIPTION FOR ASSOCIATED IMAGERY

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

# [ Helper functions ]
        
# printer to check the linked list
def print_linked_list(head : ListNode):
    current_node = head
    while current_node:
        print(current_node.val, end=(" -> "))
        current_node = current_node.next
    print("None")

class Solution():
    def delete_duplicates(self, head : ListNode) -> ListNode:
        current_node = head
        lst = []

        while current_node:
            if current_node.val not in lst:
                lst.append(current_node.val)
                prev_node = current_node
            else:
                prev_node.next = current_node.next
            current_node = current_node.next

        # print_linked_list(head)
        return head

# Test cases
solution = Solution()

# example 1
# head = ListNode(1)
# node2 = ListNode(1)
# node3 = ListNode(2)

# head.next = node2
# node2.next = node3

# example 2
# head = ListNode(1)
# node2 = ListNode(1)
# node3 = ListNode(2)
# node4 = ListNode(3)
# node5 = ListNode(3)

# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# example 3
head = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)

head.next = node2
node2.next = node3

solution.delete_duplicates(head)

# print_linked_list(head)




