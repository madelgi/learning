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


def main():
    lst = DoublyLinkedList()
    lst.append(10)
    lst.prepend(11)
    lst.prepend(-1)
    lst.append(32)
    lst.prepend(-123)
    lst.append(54)
    lst.append(123)
    lst.prepend(20)
    print str(lst)
    print "length: " + str(lst.length())
    print "found: " + str(lst.search(11).val)
#    print lst.search(-1).val
    lst.delete(11)
    print str(lst)
    print lst.length()


if __name__ == '__main__':
    main()
