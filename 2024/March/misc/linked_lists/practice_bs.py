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
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes

    def length(self):
        current = self.head
        total = 0
        while current:
            total += 1
            current = current.next
        return total

    def get(self, index):
        current = self.head
        node_index = 0
        result = ''
        if index >= self.length(): result = 'Error. Index out of bounds!'
        else:
            while True:
                print(node_index)
                if index == node_index:
                    result = current.data
                    break
                current = current.next
                node_index += 1
        return result


my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print(my_list.display())

print(my_list.length())
print(my_list.get(1))