# Queues

Various queue implementations.


## Standard Queue

A FIFO (first in first out) queue can easily be implemented as a doubly linked list:

```python
class Queue(object):
    """ A queue implemented as a doubly linked list. """
    def __init__(self, vals=None):
        if vals is None:
            self.vals = dll.DoublyLinkedList()
        else:
            self.vals = dll.from_list(vals)
```


### Operations

An efficient queue implementation should be able to perform two operations, `enqueue` and
`dequeue`, in constant time. Our doubly linked list implementation can do that.

* **Enqueue**
    * **Complexity**: `O(1)`
    * **Brief Explanation**: Our queue is implemented as a doubly linked list, and enqueue
      is equivalent to prepending a value to the doubly linked list, an operation that runs
      in O(1) time.

* **Dequeue**
    * **Complexity**: `O(1)`
    * **Brief Explanation**: Our queue is implemented as a doubly linked list, and dequeue
      is equivalent to returning the last element of the list, and reorienting the
      last element in the list to be the second to last element. Because the last element of
      a doubly linked list is accessible in constant time, both of these operations can be
      completed in constant time.


## Priority Queue

## Dequeue
