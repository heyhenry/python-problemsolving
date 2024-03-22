class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):  
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def get(self, index : int):
        error = IndexError(f'{index} out of bounds for {self}')

        if index < 0:
            raise error

        current_index = 0
        current_node = self.head

        while current_node:
            if current_index == index:
                return current_node.val
        
        if current_node is None:
            raise error
        
    def length(self):
        size = 0
        current_node = self.head
        
        while current_node:
            size += 1
            current_node = current_node.next

        return size
    
    def peek(self):
        current_node = self.head
        tail_node = None

        while current_node:
            tail_node = current_node
            current_node = current_node.next
            
        return print(tail_node.val)
    
    


ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.peek()