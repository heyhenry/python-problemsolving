# Linked Lists and Abstractions

The goal of this problem set is to be a bit more...broad with how we talk about data structures and Linked Lists, specifically in the context of abstractions and performance.  While this problem set is written for Python, it is very tricky with Python types.  I'm going to use Python type annotations heavily without any sort of typechecker, but if you really wanna "get" this, you might consider implementing these ideas in C++, Java, or another statically typed language.

I will also not be going into the many many other Abstract Data Types (ADTs) we should learn here, that can be a topic for another time.

## Linked Lists

I've implemented a Doubly Linked List class, along with a constructor definition and the `append`, `get`, `__repr__`, and `__str__` functions already implemented (the last two are great for debugging).

### Testing the Linked List

Your first task will be to implement tests for the Linked List class _before_ implementing the functions.  You need to know what you're writing before you can write it!  It's good practice to implement tests -- I've implemented one for each to get you started, but you should have 3-4 tests per method.  You can run the test script (which should fail, cause stuff is unfinished!) with `python test.py`

### Implementing the Linked List

Your second task will be to implement the remaining functions in this structure.  `linkedlist.py` contains the definition for our Linked List, and specifically you will need to implement the following functions (whose specifications are in the `linkedlist.py` file):
* `__len__`
* `peek`
* `prepend`
* `insert`
* `pop`
* `pop_front`
* `remove`

## Using the Linked List

Your third task will be to implement the following functions that use the Linked List you implemented as a way to reason about what's happening.  Note that, for these problems, you _cannot_ use the python `list`, so no using `[]` anywhere here.  All the problems and descriptions are in the `psetll.py` file.  Make sure to test them!  You should make a new test file based on `lltest.py` for this purpose

## Comparing Linked Lists and Arrays

Your fourth task will be to reimplement all of the functions inside of `psetll` using a python list instead of a linked list.  They should be very similar (if we implemented an iterator for a linked list, they would be almost identical).

### Timing Comparison

Using the `timing.py` script, hook up each of these functions to time it.  I setup constants to make this easy to change.  You will want to get times of building lists of size 100, 1000, 10000, and 100000.  Print out the times of each, and graph them.  Which data structure is better for which problem?  Why?  These are hard questions to answer, and it might partly depend on how you implemented each function!  This is just a taste of why DSA and OOP matters so much, it's...complicated.  But good luck!