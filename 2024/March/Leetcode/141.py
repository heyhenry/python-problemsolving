class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head : ListNode) -> bool:

        # result = False

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

    solution = Solution()

    # linked list cycle test case
    llwc = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    llwc.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = llwc

    # linked list no cycle test case
    llnc = ListNode(1)
    nc_node2 = ListNode(2)
    nc_node3 = ListNode(3)
    nc_node4 = ListNode(4)

    llnc.next = nc_node2
    nc_node2.next = nc_node3
    nc_node4.next = nc_node3 

    print(solution.hasCycle(llwc))
    print(solution.hasCycle(llnc))

if __name__ == "__main__":
    main()


# Notes for learning:
    
# Creating a linked list without the usage of a constructor
# class ListNode:
#     pass  # No __init__ method

# # Create nodes
# node1 = ListNode()
# node1.val = 1
# node1.next = None

# node2 = ListNode()
# node2.val = 2
# node2.next = None

# node3 = ListNode()
# node3.val = 3
# node3.next = None

# # Link nodes to form a linked list: 1 -> 2 -> 3
# node1.next = node2
# node2.next = node3
