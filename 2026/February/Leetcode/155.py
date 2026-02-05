# Leetcode No.155: Min Stack
# More Info: https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        # To track the current minimum number parallel to the original stack.
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Determine which value is the next minimum value, 
        # either the new given value or the last value in the min_stack list 
        # (which will be the smallest value in the whole list).
        if self.min_stack:
            new_min = min(val, self.min_stack[-1])
        else:
            new_min = val
        self.min_stack.append(new_min)

    def pop(self) -> None:
        # Removes the last element in the min_stack which could just be a 
        # duplicate but is done to always track and know the current minimum number 
        # in the existing original stack.
        self.min_stack.pop()
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Returns the top number (last number) in the min_stack because that will always 
        # be the current smallest (minimum) number that can be found in the original stack.
        return self.min_stack[-1]

ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin())
ms.pop()
print(ms.top())
print(ms.getMin())
