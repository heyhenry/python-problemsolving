class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def reverse_list(self, head : ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev
        return head

    def display(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


solution = Solution()

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
head = solution.reverse_list(head)
solution.display(head)