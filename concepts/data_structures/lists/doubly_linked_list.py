class Node(object):
    def __init__(self, val=None, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class DoublyLinkedList(object):
    def __init__(self, head=None, last=None):
        self.head = head
        self.last = last

    def prepend(self, val):
        """ Insert a value to the front of the list. """
        new_node = Node(val)
        if self.length() > 0:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        else:
            self.head = new_node
            self.last = self.head

    def append(self, val):
        """ Insert a value to the end of the list. """
        new_node = Node(val)
        if self.length() > 0:
            new_node.set_prev(self.last)
            self.last.set_next(new_node)
            self.last = new_node
        else:
            self.last = new_node
            self.head = self.last

    def length(self):
        """ Get the length of the list. """
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next

        return total

    def search(self, val):
        """ See if a certain value is contained within a list. """
        current = self.head
        found = False
        while current and found is False:
            if current.val == val:
                found = True
                break
            current = current.next

        if not found:
            raise ValueError("Value not present.")
        return current

    def delete(self, val):
        """ Delete the first node with value val """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.val == val:
                found = True
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("Can't delete what's not there br.")

        if previous is None:
            self.head = current.next
        else:
            previous.set_next(current.next)

    def __str__(self):
        x = self.head
        string = "["
        while x.next is not None:
            string += str(x.val) + ", "
            x = x.next

        return (string + str(self.last.val) + "]")


def from_list(lst):
    """ Convert a python list into a doubly linked list. """
    dll = DoublyLinkedList()
    for x in lst:
        dll.append(x)
    return dll


def main():
    lst = [1, 8, 23, 10, 9, 13, 142, -5, 2, 3]
    dll = from_list(lst)
    print str(dll)
    print dll.head.val
    print dll.last.val
    print dll.length()

if __name__ == '__main__':
    main()
