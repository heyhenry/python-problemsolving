class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('None')

    def length(self):
        current = self.head
        total = 0
        while current:
            total += 1
            current = current.next
        print(total)


my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.length()