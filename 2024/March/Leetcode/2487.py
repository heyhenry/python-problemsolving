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
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def remove_nodes(self, head : ListNode) -> ListNode:

        current_node = head
        lst = []
        
        while current_node:
            lst.append(current_node.val)
            current_node = current_node.next
        
        n = len(lst)

        to_remove = []

        for i in range(n):
            for j in range(i+1, n):
                if lst[i] < lst[j] and i < j:
                    if to_remove.count(lst[i]) < lst.count(lst[i]):
                        to_remove.append(lst[i])
                    break
                        
        current_node = head
        prev_node = None            
        while current_node:
            if current_node.val in to_remove:
                to_remove.remove(current_node.val)
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    head = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next
    
        return head

    def display(self, head):
        current_node = head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print('None')

solution = Solution()

data = [138,466,216,67,642,978,264,136,463,331,60,600,223,275,856,809,167,101,846,165,575,276,409,590,733,200,839,515,852,615,8,584,250,337,537,63,797,900,670,636,112,701,334,422,780,552,912,506,313,474,183,792,822,661,37,164,601,271,902,792,501,184,559,140,506,94,161,167,622,288,457,953,700,464,785,203,729,725,422,76,191,195,157,854,730,577,503,401,517,692,42,135,823,883,255,111,334,365,513,338,65,600,926,607,193,763,366,674,145,229,700,11,984,36,185,475,204,604,191,898,876,762,654,770,774,575,276,165,610,649,235,749,440,607,962,747,891,943,839,403,655,22,705,416,904,765,905,574,214,471,451,774,41,365,703,895,327,879,414,821,363,30,130,14,754,41,494,548,76,825,899,499,188,982,8,890,563,438,363,32,482,623,864,161,962,678,414,659,612,332,164,580,14,633,842,969,792,777,705,436,750,501,395,342,838,493,998,112,660,961,943,721,480,522,133,129,276,362,616,52,117,300,274,862,487,715,272,232,543,275,68,144,656,623,317,63,908,565,880,12,920,467,559,91,698]

head = ListNode(data[0])
current_node = head
for val in data[1:]:
    current_node.next = ListNode(val)
    current_node = current_node.next

# solution.display(head)
head = solution.remove_nodes(head)
solution.display(head)