class ArrayList(object):

    def __init__(self):
        self.vals = [0]*16
        self.numElts = 0

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
        list_length = len(self.vals)

    def __str__(self):
        string = "["
        i = 0
        while i < self.numElts-1:
            string += str(self.vals[i]) + ", "
            i += 1
        string += str(self.vals[i]) + "]"
        return string


def main():
    lst = ArrayList()
    for i in range(33):
        lst.append(i)
    print str(lst)


if __name__ == '__main__':
    main()
