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
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    # def reverse(self, head : ListNode) -> ListNode:
    #     curr = head
    #     prev = None
    #     while curr:
    #         next_node = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next_node
    #     head = prev
    #     return head
    
    # def remove_nodes(self, head : ListNode) -> ListNode:

    #     head = solution.reverse(head)

    #     curr = head 
    #     prev = None
    #     max_node = head.val

    #     while curr:
    #         if curr.val < max_node:
    #             if prev:
    #                 prev.next = curr.next
    #             else:
    #                 head = curr.next
    #         else:
    #             if curr.val > max_node:
    #                 max_node = curr.val
    #             prev = curr
    #         curr = curr.next
        
    #     head = solution.reverse(head)

    #     return head

    def display(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def remove_nodes(self, head : ListNode) -> ListNode:

        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev

        curr = head 
        prev = None
        max_node = head.val

        while curr:
            if curr.val < max_node:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                if curr.val > max_node:
                    max_node = curr.val
                prev = curr
            curr = curr.next
        
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev

        return head

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

solution.display(head)
head = solution.remove_nodes(head)
solution.display(head)