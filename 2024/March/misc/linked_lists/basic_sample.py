# Define a Node class to represent elements in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data for the node
        self.next = None   # Initialize the next pointer to None

# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None   # Initialize the head of the linked list to None

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        
        if not self.head:
            # If the linked list is empty, set the new node as the head
            self.head = new_node
        else:
            # If the linked list is not empty, traverse to the end and append the new node
            # The line below sets the variable 'current' to the head of the linked list.
            # This is the starting point for traversing the linked list.
            current = self.head
            # The line below initiates a 'while' loop that continues as long as the 'next' attribute
            # of the current node is not 'None'. This loop is used to traverse the linked list until 
            # the last node is reached (i.e., a node whose 'next' attribute is 'None').
            while current.next:
                # Inisde the loop, this line updates the 'current' variable to point to the next node
                # in the linked list. This effectively moves the traversal to the next node in each
                # iteration of the loop.
                current = current.next
            # Once the loop exits (when 'current.next' is 'None'), this line sets the 'next' attribute
            # of the last node (which was reached in the loop) to the new node. This effectively appends 
            # the new node to the end of the linked list.
            current.next = new_node

    def display(self):
        # Display the elements of the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None   # Initialize a variable to keep track of the previous node
        current = self.head  # Start from the head of the linked list
        
        while current:
            next_node = current.next  # Save the next node in the original list
            current.next = prev        # Reverse the link by pointing the current node to the previous node
            prev = current              # Move the previous pointer one step forward
            current = next_node        # Move the current pointer one step forward
        
        self.head = prev  # Set the head of the linked list to the last node (which was the original tail)

    def length(self):
        total = 0
        current_node = self.head
        while current_node:
            total += 1
            current_node = current_node.next
        return total

    def get(self, index):
        ll_index = 0
        current_node = self.head

        if index >= self.length(): return "Index is out of bounds!"

        while current_node:
            if index == ll_index:
                return current_node.val
            ll_index += 1
            current_node = current_node.next

    def erase(self, index):
        ll_index = 0
        current_node = self.head

        if index >= self.length(): return "Index is out of bounds!"
        
        while current_node:
            if index == ll_index:
                prev_node.next = current_node.next
            prev_node = current_node
            current_node = current_node.next
            ll_index += 1


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




    