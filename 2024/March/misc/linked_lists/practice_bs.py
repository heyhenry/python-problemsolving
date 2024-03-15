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
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")

    def length(self):
        current_node = self.head
        size = 0
        while current_node:
            size += 1
            current_node = current_node.next
        return size
    
    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def retrieve_list(self):
        current_node = self.head
        lst = []
        while current_node:
            lst.append(current_node.val)
            current_node = current_node.next
        return lst

    def get_by_index(self, index):
        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == index:
                return current_node.val
            current_node = current_node.next
            current_index += 1
        return None

    def erase(self, index):
        current_node = self.head
        current_index = 0
        prev_node = None
        while current_node:
            if current_index == index:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
            else:
                prev_node = current_node
            current_index += 1
            current_node = current_node.next

    # def delete(self, val, del_count):
    #     current_node = self.head
    #     count = 0
    #     prev_node = None
    #     while current_node:
    #         if current_node.val == val and count < del_count:
    #             count += 1
    #             if prev_node:
    #                 prev_node.next = current_node.next
    #             else:
    #                 self.head = current_node.next
    #         else:
    #             prev_node = current_node
    #         current_node = current_node.next
    
    def delete_all(self, val):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.val == val:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next

# functions to create
# append
# display
# reverse
# length
# get
# erase
# delete (with param on how many) 
# delete_all
# retrieve_list 

my_list = LinkedList()

# my_list.append(1)
# my_list.append(1)
# my_list.append(1)
my_list.append(1)
my_list.append(2)
my_list.append(1)
my_list.append(3)
my_list.append(4)

print("Display Original Linked List:")
my_list.display()

print("Length of the Linked List:")
print(my_list.length())

print("Retrieve Linked List as an array/list:")
print(my_list.retrieve_list())

print("Get node via Index (i.e. 3):")
print(my_list.get_by_index(3))

print("Remove the node in the nth location in the Linked List via index referencing (i.e. index: 1):")
my_list.erase(1)
my_list.display()

print("Reverse Original Linked List:")
my_list.reverse()
my_list.display()

print("Delete a node in Linked List:")
my_list.delete_all(1)
my_list.display()

# print("Delete specific number of nodes based on given value:")
# my_list.delete(1, 1)
# my_list.display()