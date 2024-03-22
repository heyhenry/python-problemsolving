class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):  
        self.head = None

    def append(self, val : Node):
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
        result = None
        while current_node:
            if current_index == index:
                result = current_node.val
                break
            current_index += 1
            current_node = current_node.next
        
        if current_node is None:
            raise error
        
        return result
        
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
    
    def prepend(self, val : Node):

        new_head = Node(val)
        next_node = self.head
        self.head = new_head
        self.head.next = next_node

    def insert(self, index : int, val : Node):
        new_node = Node(val)
        current_index = 0

        if index == 0:
            self.prepend(val)
        else:
            current_node = self.head
            next_node = None
            while current_node:
                current_index += 1
                if current_index == index:
                    next_node = new_node
                    next_next_node = current_node.next
                    current_node.next = next_node
                    next_node.next = next_next_node
                current_node = current_node.next

    

    def display(self):

        current_node = self.head
        while current_node: 
            print(current_node.val, end = " ->  ")
            current_node = current_node.next
        print("None")



ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.display()
ll.prepend(66)
ll.display()
ll.insert(3,21)
ll.display()
print(ll.get(3))
