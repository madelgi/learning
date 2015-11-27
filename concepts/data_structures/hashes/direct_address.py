class Element(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val


class DirectAddressTable(object):
    def __init__(self, size):
        """
        Initialize a direct address table with keys drawn from a universe
        of size `size`.
        """
        self.size = size
        self.table = [None]*size

    def __str__(self):
        string = "{"
        for elt in self.table:
            if elt:
                string += str(elt.key) + ": " + str(elt.val) + ", "

        if string == "{":
            return "{}"

        return string[:-2] + "}"

    def search(self, key):
        """
        Return the value at a certain key in the direct address table.
        """
        try:
            return self.table[key]
        except IndexError:
            return None

    def insert(self, elt):
        """
        Insert an element into our direct address table.
        """
        try:
            self.table[elt.key] = elt
        except IndexError:
            pass

    def delete(self, elt):
        """
        Remove an element from our direct address table.
        """
        try:
            self.table[elt.key] = None
        except IndexError:
            pass


def test():
    table = DirectAddressTable(10)
    print table
    e1 = Element(1, "hello")
    e2 = Element(5, 4)
    e3 = Element(2, 3.1415)
    e4 = Element(9, True)

    table.insert(e1)
    table.insert(e2)
    table.insert(e3)
    table.insert(e4)
    print table
    table.delete(e2)
    print table
    table.delete(Element(6, "blah"))
    print table
    print table.search(2).val
    print table.search(9).val
    print table.search(66)

if __name__ == '__main__':
    test()
