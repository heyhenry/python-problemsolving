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

        first_num = ''
        second_num = ''
        first = l1
        second = l2

        while first:
            first_num += str(first.val)
            first = first.next
        while second:
            second_num += str(second.val)
            second = second.next

        ans = int(first_num) + int(second_num)
        ans = str(ans)[::-1]

        head = ListNode(ans[0])
        counter = 1
        while counter < len(ans):
            new_node = ListNode(ans[counter]) 
            current = head
            while current.next:
                current = current.next
            current.next = new_node
            counter += 1

        # print(head.val)
        # curr = head
        # while curr:
        #     print(curr.val, end = " -> ")
        #     curr = curr.next
        # print("None")

        return head

        # Solution by CodingNinja.
    
        # dummy = ListNode()
        # res = dummy

        # total = carry = 0

        # while l1 or l2 or carry:
        #     total = carry

        #     if l1:
        #         total += l1.val
        #         l1 = l1.next
        #     if l2:
        #         total += l2.val
        #         l2 = l2.next

        #     num = total % 10
        #     carry = total // 10
        #     dummy.next = ListNode(num)
        #     dummy = dummy.next

        # return res.next
    
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

# solution.display(l1_head, l2_head)
solution.add_two_numbers(l1_head, l2_head)