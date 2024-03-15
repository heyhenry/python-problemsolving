# Define a Node class to represent elements in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data for the node
        self.next = None   # Initialize the next pointer to None

# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None   # Initialize the head of the linked list to None

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
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print('None')

    def retrieve_list(self):
        current_node = self.head
        lst = []
        while current_node:
            lst.append(current_node.val)
            current_node = current_node.next
        return lst

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
        if index > self.length() - 1 or index < 0:
            return print("Given index is invalid.")

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
        if val not in self.retrieve_list():
            return print("Given value is invalid.")
        
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
        if val not in self.retrieve_list():
            return print("Given value is invalid")
        
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


# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Original Linked List:")
linked_list.display()

linked_list.reverse()

print("\nReversed Linked List:")
linked_list.display()




    