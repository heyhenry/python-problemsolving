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
            # the while loop is only to loop through the linked list and place the current_node variable to the end of the linked list,
            # this is to get into a position where we can append the new_node that we have created to be added to the end (.next) of the 
            # last node that is already in the linked list!
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node # adds the newly appended node here (after the last node in the linked list)

    def display(self):
        current_node = self.head
        elems = []
        while current_node:
            elems.append(current_node.val)
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print('None')
        return elems

    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node


    def length(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        print(size)
        return size

    def get_val(self, index):
        current_node = self.head
        current_index = 0
        result = 0
        while current_node:
            if current_index == index:
                result = current_node.val
                break
            current_node = current_node.next
            current_index += 1
        print(result)
        return result

    def erase(self, index):
        current_node = self.head
        current_index = 0
        prev_node = None
        while current_node:
            if current_index == index:
                prev_node.next = current_node.next
            prev_node = current_node
            current_index += 1
            current_node = current_node.next

    # deletes every instance of given val found in the linked list
    def delete_all(self, val):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.val == val:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = None
            else:
                prev_node = current_node
            current_node = current_node.next

    def delete(self, val, count):
        current_node = self.head
        del_count = 0
        prev_node = None
        while current_node:
            if current_node.val == val and del_count < count:
                if prev_node:
                    prev_node.next = current_node.next
                    del_count += 1
                else:
                    self.head = current_node
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
# delete 

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
my_list.length()

print("Get the node value stored in the nth location via index referencing (i.e. index: 2):")
my_list.get_val(2)

# print("Remove the node in the nth location in the Linked List via index referencing (i.e. index: 1):")
# my_list.erase(1)
# my_list.display()

print("Reverse Original Linked List:")
my_list.reverse()
my_list.display()

# print("Delete a node in Linked List:")
# my_list.delete_all(1)
# my_list.display()

print("Delete specific number of nodes based on given value:")
my_list.delete(1, 3)
my_list.display()