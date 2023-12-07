class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head : ListNode) -> bool:

    result = True

    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        
        slow = slow.next
        fast = fast.next.next

    return False

def main():
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(has_cycle(node1))

if __name__ == "__main__":
    main()