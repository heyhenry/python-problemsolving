class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        lst = []
        current_node = head
        prev_node = None
        while current_node:
            if current_node.val not in lst:
                lst.append(current_node.val)
                prev_node = current_node
            else:
                prev_node.next = current_node.next
            current_node = current_node.next
        print(lst)
        return head

        cur = head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print('None')


# Test cases 
solution = Solution()

# Test case 1
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(4)
# node4 = ListNode(4)
# node5 = ListNode(5)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

head = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)

head.next = node2
node2.next = node3

solution.deleteDuplicates(head)

# current_node = head # node1 aka head
# while current_node:
#     print(current_node.val, end=" -> ")
#     current_node = current_node.next
# print("None")

