class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def remove_elements(self, head : ListNode, val : int) -> ListNode:
        curr = head
        prev = None
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr
            curr = curr.next
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
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

solution.display(head)
head = solution.remove_elements(head,6)
solution.display(head)