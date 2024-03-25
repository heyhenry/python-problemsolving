# We need generics and self-reference for Nodes
from typing import TypeVar, Self

# We need this for python generic typing
# I'm not going to go into too much detail on how this works
# But it's really important for the List ADT
T = TypeVar('T')

class LinkedList():
    """
    An implementation of a Linked List over generic type T
    Supports the usual List ADT functions
    We also include a "tail" node to help with fast peeking and popping
    """

    class Node():
        """
        Made as an inner class to make the encapsulation more sane here
        """
        # The data stored by the node
        _data : T

        # The next node in the LL
        next_node : Self | None

        def __init__(self, data : T):
            """
            Builds a node with the given data
            """
            self._data = data
            self.next_node = None

        # We have a getter for data so we can't change it
        # This allows us to make things stylistically reasonable
        @property
        def data(self) -> T:
            return self._data
        
        def __str__(self) -> str:
            return str(self._data)
        
        def __repr__(self) -> str:
            return self.__str__()

    # The head of the linked list
    _head : Node | None

    # A Pointer to the tail of the linked list
    _tail : Node | None

    def __init__(self):
        """
        Builds an empty linked list
        """
        self._head = None
        self._tail = None

    def __str__(self) -> str:
        """
        Converts this Linked List to a string of the form
        LL( - data1 - data2 - ... - tail - )
        """
        result = "LL( - "
        current = self._head
        while current is not None:
            result += str(current) + " - "
            current = current.next_node
        result += ")"
        return result
    
    def __repr__(self) -> str:
        return str(self)
    
    def append(self, item : T):
        """
        Adds an item to the end of this Linked List
        LL( - 1 - 2 - ).append(5) results in LL( - 1 - 2 - 5 - )
        """
        # note that we need to use `self` to access the inner class
        node = self.Node(item)

        if self._head is None:
            # since both are node, we're good
            self._head = node
            self._tail = node

        else:
            # first update our tail pointer
            self._tail.next_node = node
            # then set the class pointer
            self._tail = node

    def get(self, index : int) -> T:
        """
        Gets a given element from this linked list
        Note that negative indexing is not supported (extra credit?)
        """
        error = IndexError(f'{index} out of bounds for {self}')

        if index < 0:
            raise error
        
        current = self._head
        count = 0
        
        while count < index:
            if current is None:
                raise error
            current = current.next_node
            count += 1

        if current is None:
            raise error
        
        return current.data
    
    # Everything after this comment is for you to implement :)

    def __len__(self) -> int:
        """
        Returns the number of elements in this LL
        length(LL( - 3 - 7 - )) returns 2
        """
        current = self._head
        size = 0

        while current:
            size += 1
            current = current.next_node

        return size

    def peek(self) -> T:
        """
        Returns the last element of this LL
        If this LL is empty, instead raises an IndexError
        This is faster than using `get` since we can avoid traversing forward
        LL( - 3 - 7 - ).peek() returns 7
        """
        current_node = self._head
        last_element = 0
        while current_node:
            last_element = current_node.data
            current_node = current_node.next_node
        return last_element

    def prepend(self, item : T):
        """
        Adds an element to the beginning of this linked list
        LL( - 1 - 2 - ).prepend(5) results in LL( - 5 - 1 - 2 - )
        """
        pass

    def insert(self, index : int, item : T):
        """
        Inserts an element in the given index of this linked list
        LL( - 3 - 4 - ).insert(1, 5) results in LL( - 3 - 5 - 4 - )
        """
        pass

    def pop(self) -> T:
        """
        Removes and returns the last element of this linked list (the tail)
        If this LL is empty, instead raises an IndexError
        Note that if we empty the list, the head should also be made null

        LL( - 3 - 7 - ).pop() returns 7, and ends with LL( - 3 - )
        """
        pass

    def pop_front(self) -> T:
        """
        Removes and returns the _first_ element of this linked list (the head)
        If this LL is empty, instead raises an IndexError
        Note that if we empty the list, the tail should also be made null

        LL( - 3 - 7 - ).pop_front() returns 3, and ends with LL( - 7 - )
        """
        pass

    def remove(self, index : int):
        """
        Removes the element at the given index of this Linked List
        If the given index is out of bounds instead raises an IndexError
        Note that if we empty the list, the head and tail should both be null

        LL( - 3 - 7 - 5 - ).remove(1) ends with LL( - 3 - 7 - )
        """
        pass