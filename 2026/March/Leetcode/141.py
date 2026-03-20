# Leetcode No.141: Linked List Cycle
# More Info: https://leetcode.com/problems/linked-list-cycle/description/
# Additional resources 1: https://www.youtube.com/watch?v=S5TcPmTl6ww 
# Additional resources 2: https://www.w3schools.com/python/python_dsa_linkedlists.asp

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def has_cycle(self, head : ListNode) -> bool:
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False

# example 1: head = [3,2,0,-4], pos = 1
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4

# from desc: "Internally, pos is used to denote the index of the node that tail's next pointer is connected to."
node4.next = node2

# node 1 is the head node (start of the linked list)
sol = Solution()

print(sol.has_cycle(node1))