"""
83. Remove Duplicates from Sorted List

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
class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def delete_duplicates(self, head : ListNode) -> ListNode:

        uniq = []
        curr = head
        prev = None
        while curr:
            if curr.val not in uniq:
                uniq.append(curr.val)
                prev = curr
            else:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            curr = curr.next
        return head

    def display(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

head = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)

head.next = node2
node2.next = node3

solution = Solution()

head = solution.delete_duplicates(head)
solution.display(head)