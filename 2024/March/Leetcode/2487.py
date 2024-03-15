"""
2487. Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""
class ListNode():
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution():
    def remove_nodes(self, head : ListNode) -> ListNode:

        # seems like a good solution aside from the time limit exceeded trigger
        # current_node = head
        # lst = []
        
        # while current_node:
        #     lst.append(current_node.val)
        #     current_node = current_node.next
        
        # n = len(lst)

        # to_remove = []

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if lst[i] < lst[j] and i < j:
        #             if to_remove.count(lst[i]) < lst.count(lst[i]):
        #                 to_remove.append(lst[i])
        #             break
                        
        # current_node = head
        # prev_node = None            
        # while current_node:
        #     if current_node.val in to_remove:
        #         to_remove.remove(current_node.val)
        #         if prev_node:
        #             prev_node.next = current_node.next
        #         else:
        #             head = current_node.next
        #     else:
        #         prev_node = current_node
        #     current_node = current_node.next
    
        # return head     

        # Actual solution that is within efficient time complexity to pass on leetcode
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
        curr_max = head.val
        while curr:
            if curr.val < curr_max:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                if curr.val > curr_max:
                    curr_max = curr.val
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
        current_node = head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print('None')

solution = Solution()

data = [5,2,13,3,8]

head = ListNode(data[0])
current_node = head
for val in data[1:]:
    current_node.next = ListNode(val)
    current_node = current_node.next

# solution.display(head)
head = solution.remove_nodes(head)
solution.display(head)