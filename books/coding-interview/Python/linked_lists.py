import sys
sys.path.insert(0, '/Users/maxdelgiudice/learning/concepts/data_structures/lists')
import singly_linked_list as s


def remove_dups(lst):
    """
    Problem 2.1: Remove duplicates from an unsorted linked list.
    """
    data = {}
    current_node = lst.head
    next_node = None
    if current_node is None:
        return lst
    else:
        data[current_node.val] = 1

    while next_node is not None:
        if next_node.val in data:
            current_node.next = next_node.next
            current_node = current_node.next
            if next_node.next is not None:
                next_node = next_node.next.next
        else:
            current_node = current_node.next
            next_node = next_node.next

    return lst


def nth_to_last(lst, n):
    """
    Problem 2.2: Implement an algorithm to find the nth to last element of a
    singly linked list. (Completed)
    """
    list_length = lst.length()
    current = lst.head
    for i in range(list_length - n):
        current = current.next
    return current.val


def delete(lst, val):
    """
    Problem 2.3: Implement an algorithm to delete a node in the middle of a
    single linked list, given only access to that node.
    """
    current = lst.head
    if current.val == val:
        return s.SinglyLinkedList()
    next_node = current.next
    while next_node is not None:
        if next_node.val is val:
            current.next = next_node.next
            break
        current = current.next
        next_node = next_node.next

    return lst


def add_lists(lst1, lst2):
    """
    Problem 2.4: You have two numbers represented by a linked list, where each
    node contains a single digit. The digits are stored in reverse order, such
    that the 1's digit is at the head of the list. Write a function that adds
    the two numbers and returns the sum as a linked list.
    """
    return 0


def circular_node(lst):
    """
    Problem 2.5: Given a circular linked list, implement an algorithm which
    returns node at the beginning of the loop.
    """
    return 0


def main():
    sll = s.from_list([1, 5, 23, -10, 2, 2, 5, 132, 17, -32, -1, -1, 2])
    print nth_to_last(sll, 3)
    print nth_to_last(sll, 5)
    print sll
    delete(sll, 132)
    print sll
    return 0


if __name__ == '__main__':
    main()
