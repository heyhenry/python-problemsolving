class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
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
        max_val = head.val
        while curr:
            if curr.val < max_val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                if curr.val > max_val:
                    max_val = curr.val
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

    def display(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
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

solution.display(head)
head = solution.remove_nodes(head)
solution.display(head)
