"""
Math 590
Project 2
Fall 2019

p2queue.py

Partner 1: Yuhang Liu (yl655)
Partner 2: Kuan Wang (kw300)
Date: 2019.11.08
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 100.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.queue)
        print('Front: %d' % self.front)
        print('Rear: %d' % self.rear)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        if self.numElems == len(self.queue):
            return True
        else:
            return False

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0:
            return True
        else:
            return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        # Reset the front to index 0
        if self.rear <= self.front:
            self.queue = self.queue[self.front:] + self.queue[:self.rear]
        self.front = 0
        self.rear = self.numElems
        # Resize it
        self.queue = self.queue + [None for x in self.queue]
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # Before push we need to check whether the queue is full
        if self.isFull():
            self.resize()
        # Put the element in the rear and increase the size
        # Since the element may wrap back to the front, we need to increase the rear index mod the size of the queue
        self.queue[self.rear] = val
        self.rear = (self.rear + 1) % len(self.queue)
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        # Get the last element and change the position into None
        # Since the element may wrap back to the front, we need to decrease the rear index mod the size of the queue
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.numElems -= 1
        return temp
