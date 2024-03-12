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

    def erase(self, index):
        current = self.head
        node_index = 0
        result = ''
        boundary_error = False
        if index >= self.length(): boundary_error = True
        else:
            while True:
                # save the current node -> last_node
                last_node = current
                current = current.next
                if index == node_index:
                    last_node.next = current.next # <-- still working on getting deep understanding of this line's logic
                    break
                node_index += 1
        if boundary_error:
            result = 'Error. Out of bounds!'
        else:
            result = self.display()

        return result



my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print(my_list.display())

# print(my_list.length())
# print(my_list.get(1))
print(my_list.erase(1))