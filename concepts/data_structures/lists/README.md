# Lists

Various list implementations.

## Singly Linked List

Singly linked lists are one of the simplest possible data structures. The building blocks of
a list, `Nodes`, contain a value and a pointer to the next Node:

```python
class Node(object):
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node
```

The actual linked list just contains a reference to a single node, the `head` of the list:

```python
class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
```

A singly linked list can be visualized as a sequence of nodes terminated by a null reference:

```
         | 3 | o~|~~~>| 4 | o~|~~~>| 5 | o~|~~~>|x|
           ^                                     ^
list head _|                 null (end of list) _|
```

Each node contains a value and a pointer to the next node, as discussed earlier.


### Operations

* **Prepend**
    * **Complexity**: `O(1)`
    * **Brief Explanation**: The linked list simply maintains which node is the head, so
    `insert` just replaces the head with our new node, and sets that node's `next` value
    to the previous head.

* **Append**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Have to iterate through the entire list until we reach the last
    node, and then append the new value to the end.

* **Size**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: `size` visits every node in order to count the number of nodes.

* **Search**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Worst-case scenario, `search` visits every node.

* **Delete**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Worst-case scenario, `delete` visits every node.


### Additional Notes

We can modify our singly linked list definition such that, rather than terminating in a
null pointer, the last node in the list points back to the head. This is called a **Circular
linked list**:

```
         | 3 | o |<~~~>| 4 | o |<~~>| 5 | o~|
           ^                              |
           |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
```

Circularly linked lists can be a good choice for representing structures that can naturally be
viewed as circular, e.g. the corners of a polygon.

## Doubly linked list

We can modify our node definition to keep track of both the previous node and the next node:

```python
class Node(object):
    def __init__(self, val=None, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node
```

If we modify our list to include a reference to both the head and the last node, we
then have a doubly linked list:

```python
class DoublyLinkedList(object):
    def __init__(self, head=None, last=None):
        self.head = head
        self.last = last
```

Visually, our list looks something like:

```
|x<|~~~|>3 | o<|~~~|>4 | o<|~~~|>5 | o<|~~~|>x|
```


### Operations

* **Prepend**
    * **Complexity**: `O(1)`
    * **Brief Explanation**: The doubly linked list maintains which node is the head, so
    `insert` just replaces the head with our new node, and sets that node's `next` value
    to the previous head and `prev` value to null.

* **Append**
    * **Complexity**: `O(1)`
    * **Brief Explanation**: Unlike a singly linked list, a doubly linked list keeps track
      of the last node in the list. Therefore, we can simply replace that value with our
      new last value.

* **Size**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: `size` visits every node in order to count the number of nodes.

* **Search**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Worst-case scenario, `search` visits every node.

* **Delete**
    * **Complexity**: `O(n)`
    * **Brief Explanation**: Worst-case scenario, `delete` visits every node.


## Dynamic Array


### Operations

* **Prepend**: O(n)
* **Append**: O(1) (usually)
  **Brief Explanation**: Generally, assuming the array has not run out of space, appending a
    value to the end is as simple as doing a single `arr[index] = val`. However, if our array
    is out of space, we have to create a new array that is double the size of our old one,
    copy the old values over, and place our new value at the end. In this case, ``append`` is
    ``O(n)``.
* **Size**: O(1)
  **Brief Explanation**: The data structure itself maintains an attribute that  keeps track
    of the number of elements.
* **Search**
* **Delete**
