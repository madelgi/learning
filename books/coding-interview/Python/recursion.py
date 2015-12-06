def fib(num):
    """
    Problem 8.1: Write a method to generate the nth Fibonacci number.
    """
    def fib_help(num, n1, n2):
        if num == 0:
            return n1
        else:
            return fib_help(num-1, n2, n1+n2)

    return fib_help(num, 0, 1)


def robot_grid(n):
    """
    Problem 8.2: Imagine a robot sitting on the upper left hand corner of an
    NxN grid. The robot can only move in two directions: right and down. How
    many possible paths are there for the robot?
    """
    return 0


def subsets(lst):
    """
    Problem 8.3: Write a method that returns all subsets of a set.
    """
    return 0


def string_perms(string):
    """
    Problem 8.4: Write a method to compute all permutations of a string.
    """
    return 0

def paint_fill(array, point, color):
    y = point[0]
    x = point[1]

    old_color = array[y][x]
    array[y][x] = color
    if array[y+1][x] == old_color:
        return paint_fill(array, [y+1, x], color)
    if array[y-1][x] == old_color:
        return paint_fill(array, [y-1, x], color)
    if array[y][x+1] == old_color:
        return paint_fill(array, [y, x+1], color)
    if array[y][x-1] == old_color:
        return paint_fill(array, [y, x-1], color)
    if array[y+1][x+1] == old_color:
        return paint_fill(array, [y+1, x+1], color)
    if array[y-1][x-1] == old_color:
        return paint_fill(array, [y-1, x-1], color)
    if array[y-1][x+1] == old_color:
        return paint_fill(array, [y-1, x+1], color)
    if array[y+1][x-1] == old_color:
        return paint_fill(array, [y+1, x-1], color)

    return array
