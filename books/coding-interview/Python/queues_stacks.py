import sys
sys.path.insert(0, '~/learning/concepts/data_structures/queues')
sys.path.insert(0, '~/learning/concepts/data_structures/stacks')
# import queue as q
import stack as s

def min_stack(stack):
    """
    Problem 3.2: How would you design a stack which, in addition to push and
    pop, also has a function min which returns the minimum element? Push, pop,
    and min should all operate in O(1) time.

    Answer: Just keep track of the min via the data structure itself?
    """
    return 0


class MyQueue(object):
    """
    Problem 3.5: Implement a queue using two stacks.
    """
    def __init__(self):
        self.en_stack = s.Stack()
        self.de_stack = s.Stack()

    def enqueue(self, val):
        self.en_stack.push(val)

    def dequeue(self):
        if self.de_stack.is_empty():
            if self.en_stack.is_empty():
                return ValueError("Nothin in yr queue, brah.")
            while not self.en_stack.is_empty():
                self.de_stack.push(self.en_stack.pop())

        return self.de_stack.pop()


def sort_stack(stack):
    """
    Problem 3.6: Sort a stack in ascending order using only the functions
    ``push``, ``pop``, ``peek``, and ``is_empty``.
    """
    return 0
