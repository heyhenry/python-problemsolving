class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        current_node = self.head
        lst = []
        while current_node:
            lst.append(current_node.val)
            current_node = current_node.next
        return print(lst)
    
    def get_list(self):
        current_node = self.head
        lst = []
        while current_node:
            lst.append(current_node.val)
            current_node = current_node.next
        return lst

class Solution:
    def addTwoNumbers(self, l1 : LinkedList, l2 : LinkedList) -> LinkedList:
        first_num = ''
        second_num = ''

        for i in l1.get_list():
            first_num += str(i)
        for i in l2.get_list():
            second_num += str(i)

        total = str(int(first_num) + int(second_num))
        total = total[::-1]

        l3 = LinkedList()
        for i in total:
            l3.append(int(i))

        return print(l3.display())

l1 = LinkedList()
l2 = LinkedList()
my_solution = Solution()

l1.append(2)
l1.append(4)
l1.append(3)

l2.append(5)
l2.append(6)
l2.append(4)

l1.display()
l2.display()

# print(l1.get_list())
# print(l2.get_list())

my_solution.addTwoNumbers(l1, l2)