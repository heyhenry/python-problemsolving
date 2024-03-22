from linkedlist import LinkedList

def put_in_front(s : str, ll : LinkedList[str]):
    """
    Puts all the given characters from the given string `s`
    In front of the linked list `ll` in _reverse_ order

    Examples:
        lst = LL( - a - b - c - )
        put_in_front('hello', lst)
        produces LL( - o - l - l - e - h - a - b - c - )

        lst = LL( - )
        put_in_front('a', lst)
        produces LL( - a - )
    """
    pass

def reverse(ll : LinkedList[int]):
    """
    Reverses the order of the linked list `ll`

    Examples:
        lst = LL( - 5 - 3 - 9 - 1 )
        reverse(lst)
        produces LL( - 1 - 9 - 3 - 5 - )

        lst = LL( - )
        reverse(lst)
        produces LL( - )
    """
    pass

def prod_elements(ll : LinkedList[int]):
    """
    Returns the product of all elements in the LL
    Returns `1` if there are no elements in the linked list

    Examples:
        prod(LL( - 5 - 3 - 1 )) --> 15
        prod(LL( - )) --> 1
        prod(LL( - -5 - 9 - 17 - 0 - 5 )) --> 0
    """
    pass

# All the following functions are for the list implementations of the above
# These are for the "fourth task" and timing

def put_in_front_lst(s : str, lst : list[str]):
    """
    Puts all the given characters from the given string `s`
    In front of the `lst`

    Examples:
        lst = ['a', 'b', 'c']
        put_in_front('hello', lst)
        ['o', 'l', 'l', 'e', 'h', 'a', 'b', 'c']

        lst = []
        put_in_front('a', lst)
        ['a']
    """
    pass

def reverse(lst : list[int]):
    """
    Reverses the order of the 'lst'

    Examples:
        lst = [5, 3, 9, 1]
        reverse(lst)
        [1, 9, 3, 5]

        lst = []
        reverse(lst)
        []
    """
    pass

def prod_elements(lst : list[int]):
    """
    Returns the product of all elements in the lst
    Returns `1` if there are no elements in the list

    Examples:
        prod([5, 3, 1]) --> 15
        prod([]) --> 1
        prod([-5, 9, 17, 0, 5]) --> 0
    """
    pass