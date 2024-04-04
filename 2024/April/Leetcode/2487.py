"""
2487. Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def remove_nodes(self, head : ListNode) -> ListNode:

        # Reverse linked list
        current_node = head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        head = prev_node

        # Coding logic for given problem
        max_val = head.val
        current_node = head
        prev_node = None
        while current_node:
            if max_val > current_node.val:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    head = current_node.next
            else:
                if current_node.val > max_val:
                    max_val = current_node.val
                prev_node = current_node
            current_node = current_node.next
        
        # Reverse linked list back to original order
        current_node = head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        head = prev_node

        return head
    
    def display(self, head):
        current_node = head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")

head = ListNode(5)
node2 = ListNode(2)
node3 = ListNode(13)
node4 = ListNode(3)
node5 = ListNode(8)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
head = solution.remove_nodes(head)
solution.display(head)
