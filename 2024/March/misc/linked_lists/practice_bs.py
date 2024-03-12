class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        print(nodes)
        return nodes
    
    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1
        # print(count)
        return count

    def get(self, index):
        lst_index = 0
        current_node = self.head
        out_of_bounds = False
        result = 0
        if index >= self.length(): out_of_bounds = True
        else:
            while True:
                if index == lst_index:
                    result = current_node.data
                    break
                current_node = current_node.next
                lst_index += 1
        if out_of_bounds:
            result = 'Error! Index out of bounds.'

        # print(result)
        return result
    
    def erase(self, index):
        lst_index = 0
        current = self.head
        out_of_bounds = False
        result = ''
        if index >= self.length(): out_of_bounds = True
        else:
            while True:
                if index == lst_index:
                    prev_node.next = current.next
                    break
                prev_node = current
                current = current.next
                lst_index += 1
        if out_of_bounds:
            result = 'Error! Index out of bounds.'
        
        return result

my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
my_list.length()
my_list.get(2)
my_list.erase(2)
my_list.display()