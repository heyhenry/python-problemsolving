class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    def has_cycle(self, head : ListNode) -> bool:
        # if not head or not head.next:
        #     print('yes')
        #     return False

        # slow_ptr = head
        # fast_ptr = head.next

        # while fast_ptr.next and fast_ptr.next.next:
        #     if slow_ptr == fast_ptr:
        #         print('no')
        #         return True
        #     slow_ptr = slow_ptr.next
        #     fast_ptr = fast_ptr.next.next
        # print('fckyes')
        # return False

        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

    def display(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

solution = Solution()

head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(solution.has_cycle(head))