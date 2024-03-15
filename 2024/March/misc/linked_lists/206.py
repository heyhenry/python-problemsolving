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

    def display(self, head):
        current_node = head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
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