from random import randint
from time import time_ns
from linkedlist import LinkedList
import psetll

# The size of the linked list or python list
LIST_SIZE = 100
# Whether to use a linked list or the python list for timing
USE_LL = True

# Which function to use
FUNCTION = psetll.put_in_front_lst
# Whether or not we also need to build a string (for put in front)
STRING_NEEDED = True

# How many iterations to run the test
# Can lower to 50 safely if things are slow
ITERATIONS = 200

def main():
    for _ in range(int(1e6)):
        #spin for a bit to help with timing
        pass

    times = []
    for _ in range(ITERATIONS):
        lst = LinkedList() if USE_LL else []
        for _ in range(LIST_SIZE):
            # Use randomness to avoid weird timing stuff
            # Note that we can interchangeably use `append`, wow!
            lst.append(randint(0, 1000))
        if STRING_NEEDED:
            s = ""
            # random strings
            for _ in range(LIST_SIZE):
                s += chr(randint(ord('a'), ord('z')))
        current = time_ns()
        FUNCTION(*((s, lst) if STRING_NEEDED else lst))
        final = time_ns()
        times.append(final - current)
    avg = sum(times) / ITERATIONS
    avg_s = avg / 1e9
    print(f'Average time across {ITERATIONS} iterations was {avg_s} when using a ' +
        ("Linked List" if USE_LL else "Python List"))

if __name__ == "__main__":

    main()