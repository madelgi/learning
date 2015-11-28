class ArrayList(object):
    def __init__(self):
        self.vals = [0]*16
        self.numElts = 0

    def __str__(self):
        string = "["
        i = 0
        while i < self.numElts-1:
            string += str(self.vals[i]) + ", "
            i += 1
        string += str(self.vals[i]) + "]"
        return string

    def prepend(self, val):
        new_array = [0]*len(self.vals)
        if self.numElts == len(self.vals):
            new_array *= 2
        new_array[0] = val
        for i in xrange(0, self.numElts):
            new_array[i+1] = self.vals[i]

        self.numElts += 1
        self.vals = new_array

    def append(self, val):
        list_length = len(self.vals)

        if self.numElts >= list_length:
            biggerList = [0]*(2*list_length)
            i = 0
            while i < list_length:
                biggerList[i] = self.vals[i]
                i = i+1
            self.vals = biggerList

        self.vals[self.numElts] = val
        self.numElts = self.numElts + 1

    def search(self, val):
        for i in range(self.numElts):
            if self.vals[i] == val:
                return val
        return ValueError("Value not found, br.")

    def delete(self, val):
        for i in range(self.numElts):
            # we just delete the first instance of the element.
            if self.vals[i] == val:
                self.vals = self.vals[:i-1] + self.vals[i:]
                self.numElts -= 1
        return ValueError("Value not found, br.")


def main():
    lst = ArrayList()
    for i in range(10):
        lst.append(i)
    print str(lst)
    lst.prepend(2)
    print str(lst)
    lst.prepend(1)
    print str(lst)
    lst.prepend(-10)
    lst.delete(5)
    print str(lst)


if __name__ == '__main__':
    main()
