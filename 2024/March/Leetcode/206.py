"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def reverse_list(self, head : ListNode) -> ListNode:
        current_node = head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        head = prev_node
        return head

        # to check the altered(reversed) linked list
        cur = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print('None')

    def display(self, head):
        current_node = head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print('None')

solution = Solution()

# example 1
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution.display(head)
solution.reverse_list(head)
solution.display(head)