from typing import TypeVar
from linkedlist import LinkedList

T = TypeVar('T')

def error(expected, given, result : bool) -> bool:
    assert isinstance(result, bool)
    if result:
        raise AssertionError(f'Expected {repr(expected)}, got {repr(given)}')
    return result

def assert_none(given : None) -> bool:
    return error(None, given, not given is None)

def assert_true(given : bool) -> bool:
    return error(True, given, not given)

def assert_false(given : bool) -> bool:
    return error(False, given, given)

def assert_eq(expected, given) -> bool:
    result = expected != given
    return error(expected, given, result)

def constructor_tests():
    ll = LinkedList()
    assert_none(ll._head)
    assert_none(ll._tail)

def append_tests():
    ll1 = LinkedList[int]()
    ll2 = LinkedList[str]()

    ll1.append(5)
    assert_eq(5, ll1._head.data)
    assert_eq(5, ll1._tail.data)
    assert_none(ll2._head)

    ll2.append('hello')
    ll2.append(' ')
    ll2.append('world')
    assert_eq('hello', ll2._head.data)
    assert_eq('world', ll2._tail.data)

def get_tests():
    ll1 = LinkedList[int]()
    ll2 = LinkedList[str]()

    ll1.append(5)
    assert_eq(5, ll1.get(0))

    ll2.append('hello')
    ll2.append(' ')
    ll2.append('world')
    assert_eq('hello', ll2.get(0))
    assert_eq(' ', ll2.get(1))
    assert_eq('world', ll2.get(2))

    try:
        ll1.get(2)
        raise AssertionError(f'Expected IndexError when testing {ll1} with 2')
    except IndexError:
        pass

    try:
        ll2.get(-1)
        raise AssertionError(f'Expected IndexError when testing {ll2} with -1')
    except IndexError:
        pass

    ll3 = LinkedList()
    try:
        ll3.get(0)
        raise AssertionError(f'Expected IndexError when testing {ll3} with 0')
    except IndexError:
        pass

def str_tests():
    ll1 = LinkedList[int]()
    ll2 = LinkedList[str]()
    ll3 = LinkedList()

    ll1.append(5)
    ll1.append(8)
    ll1.append(-3)

    ll2.append('hello')
    ll2.append(' ')
    ll2.append('world')

    assert_eq('LL( - 5 - 8 - -3 - )', str(ll1))
    assert_eq('LL( - hello -   - world - )', str(ll2))
    assert_eq('LL( - )', str(ll3))

def len_tests():
    ll1 = LinkedList[int]()

    ll1.append(3)
    ll1.append(7)

    assert_eq(2, len(ll1))

def peek_tests():
    ll1 = LinkedList[int]()

    ll1.append(3)
    ll1.append(7)

    assert_eq(7, ll1.peek())
    assert_eq(ll1.peek(), ll1._tail.data)

def prepend_tests():
    ll1 = LinkedList[int]()

    ll1.append(1)
    ll1.append(2)
    ll1.prepend(5)

    assert_eq(2, ll1.peek())
    assert_eq(5, ll1.get(0))

def insert_tests():
    ll1 = LinkedList[int]()

    ll1.append(3)
    ll1.append(4)
    ll1.insert(2, 5)

    assert_eq(4, ll1.peek())
    assert_eq(5, ll1.get(1))

def pop_tests():
    ll1 = LinkedList[int]()

    ll1.append(3)
    ll1.append(7)

    result = ll1.pop()
    assert_eq(7, result)
    assert_eq(3, ll1.get(0))
    assert_eq(1, len(ll1))

def pop_front_tests():
    ll1 = LinkedList[int]()

    ll1.append(3)
    ll1.append(7)

    result = ll1.pop_front()
    assert_eq(3, result)
    assert_eq(7, ll1.get(0))
    assert_eq(1, len(ll1))

def remove_tests():
    ll1 = LinkedList[int]()

    ll1.append(3)
    ll1.append(7)
    ll1.append(5)

    ll1.remove(1)
    assert_eq(3, ll1.get(0))
    assert_eq(5, ll1.get(1))
    assert_eq(2, len(ll1))

def linked_list_tests():
    constructor_tests()
    print("  Constructor tests Passed")
    append_tests()
    print("  Append tests passed")
    get_tests()
    print("  Get tests passed")
    str_tests()
    print("  String tests passed")
    len_tests()
    print("  Length tests passed")
    peek_tests()
    print("  Peek tests passed")
    prepend_tests()
    print("  Prepend tests passed")
    insert_tests()
    print("  Insert tests passed")
    pop_tests()
    print("  Pop tests passed")
    pop_front_tests()
    print("  Pop Front tests passed")
    remove_tests()
    print("  Remove tests passed")

def test():
    print("Linked List tests")
    linked_list_tests()
    print("All tests passed")

if __name__=="__main__":
    test()