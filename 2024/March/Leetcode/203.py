"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def remove_elements(self, head : ListNode, val : int) -> ListNode:
        current_node = head
        prev_node = None
        while current_node:
            if current_node.val == val:
                if prev_node:     
                    prev_node.next = current_node.next
                else:
                    head = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next

        # To display altered linked list
        # cur = head
        # while cur:
        #     print(cur.val, end=" -> ")
        #     cur = cur.next
        # print('None')
        
solution = Solution()

# example 1
# head = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(6)
# node4 = ListNode(3)
# node5 = ListNode(4)
# node6 = ListNode(5)
# node7 = ListNode(6)

# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7

# example 2
# head = None

# example 3
head = ListNode(7)
node2 = ListNode(7)
node3 = ListNode(7)
node4 = ListNode(7)

head.next = node2
node2.next = node3
node3.next = node4

solution.remove_elements(head,7)

# cur = head
# while cur:
#     print(cur.val, end=" -> ")
#     cur = cur.next
# print('None')
