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
        elems = []
        while current_node:
            elems.append(current_node.val)
            current_node = current_node.next
        return elems

    def length(self):
        current_node = self.head
        total = 0
        while current_node:
            total += 1
            current_node = current_node.next
        return total
    
    def get(self, index):
        index_counter = 0
        current_node = self.head
        if index >= self.length(): return "Index out of bounds!"
        while current_node:
            if index == index_counter:
                return current_node.val
            current_node = current_node.next
            index_counter += 1

    def erase(self, index):
        index_counter = 0
        current_node = self.head
        if index >= self.length(): return "Index out of bounds!"
        # prev_node = None
        while current_node:
            if index == index_counter:
                prev_node.next = current_node.next
            prev_node = current_node
            current_node = current_node.next
            index_counter +=1

    # save the next node in the original list
    # reverse the link by pointing the current node to the previous node
    # move the previous pointer one step forward
    # move the current pointer one step forward
    # set the starting head to be the last node
    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

# functions to create
# append
# display
# reverse
# length
# get
# erase

my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print("Display Original Linked List:")
print(my_list.display())

# print("Display Reversed Linked List:")
# my_list.reverse()
# print(my_list.display())

print("Length of the Linked List:")
print(my_list.length())

print("Get the node value stored in the nth location via index referencing (i.e. index: 2):")
print(my_list.get(2))

print("Remove the node in the nth location in the Linked List via index referencing (i.e. index: 1):")
my_list.erase(1)
print(my_list.display())

print("Reverse Original Linked List:")
my_list.reverse()
print(my_list.display())