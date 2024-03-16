"""
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 
Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def pair_sum(self, head : ListNode) -> int:

        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        twin_sums = []
        n = len(lst)
 
        for i in range(int(n/2)):
            twin_sums.append(lst[i] + lst[n-1])
            n -= 1
        
        return max(twin_sums)

    def get_size(self, head):
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        return size



head = ListNode(5)
node2 = ListNode(4)
node3 = ListNode(2)
node4 = ListNode(1)

head.next = node2
node2.next = node3
node3.next = node4

sol = Solution()

print(sol.pair_sum(head))
