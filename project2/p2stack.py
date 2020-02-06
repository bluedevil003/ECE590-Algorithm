"""
Math 590
Project 2
Fall 2019

p2stack.py

Partner 1: Yuhang Liu (yl655)
Partner 2: Kuan Wang (kw300)
Date: 2019.11.08
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 100.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=100):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.stack)
        print('Top: %d' % self.top)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        if len(self.stack) == self.numElems:
            return True
        else:
            return False

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0:
            return True
        else:
            return False

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        self.stack += [None for x in self.stack]
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # Before push we need to check whether the stack is full
        if self.isFull():
            self.resize()
        # Put the element at the top of it and increase the size
        self.top += 1
        self.stack[self.top] = val
        self.numElems += 1
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        # Remove the top element and decrease the size by one.
        temp = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        self.numElems -= 1
        return temp
