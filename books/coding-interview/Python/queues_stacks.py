import sys
sys.path.insert(0, '~/learning/concepts/data_structures/queues')
sys.path.insert(0, '/Users/maxdelgiudice/learning/concepts/data_structures/stacks')
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
    asc_stack = s.Stack()
    temp_stack = s.Stack()
    while not stack.is_empty():
        val = stack.peek()
        if asc_stack.is_empty():
            asc_stack.push(stack.pop())
            continue

        if val > asc_stack.peek():
            asc_stack.push(stack.pop())
        else:
            while (asc_stack.peek() > val and not asc_stack.is_empty()):
                temp_stack.push(asc_stack.pop())
            asc_stack.push(stack.pop())
            while not temp_stack.is_empty():
                asc_stack.push(temp_stack.pop())


def test():
    stack = s.Stack()
    stack.push(3)
    stack.push(10)
    stack.push(-1)
    stack.push(32)
    stack.push(11)
    stack.push(5)
    print stack
    sorted_stack = sort_stack(stack)
    print sorted_stack


if __name__ == '__main__':
    test()
