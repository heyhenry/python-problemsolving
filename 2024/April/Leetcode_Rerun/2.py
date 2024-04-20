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

        num1 = ''
        num2 = ''

        curr = l1
        while curr:
            num1 += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next
        
        total = [int(i) for i in str(int(num1[::-1]) + int(num2[::-1]))[::-1]] 
        n = len(total)

        head = ListNode(total[0])
        
        curr = head
        
        for i in range(1, n):
            while curr.next:
                curr = curr.next
            curr.next = ListNode(total[i])
        
        # self.display(head)
        return head
        
    def display(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

head_1 = ListNode(2)
node2_1 = ListNode(4)
node3_1 = ListNode(3)

head_1.next = node2_1
node2_1.next = node3_1

head_2 = ListNode(5)
node2_2 = ListNode(6)
node3_2 = ListNode(4)

head_2.next = node2_2
node2_2.next = node3_2

solution = Solution()

solution.add_two_numbers(head_1, head_2)