import random
import time


def bubble_sort(nums):
    """ Bubble sort implementation. """
    compare_len = len(nums)
    while compare_len > 1:
        for i in range(compare_len - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        compare_len -= 1

    return nums


def insertion_sort(nums):
    """ Insertion Sort implementation. """
    list_len = len(nums)
    for i in range(1, list_len):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= j-1

    return nums


def merge_sort(nums):
    """ Merge sort implementation. """
    list_len = len(nums)
    if list_len < 2:
        return nums

    left = []
    right = []
    mid = list_len/2
    for x in nums[:mid]:
        left.append(x)
    for x in nums[mid:]:
        right.append(x)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if left:
        result + left
    if right:
        result + right
    return result


def quick_sort(nums):
    def partition(nums):
        """
        Take an array ``nums`` and and index 0 <= n < length(nums), and sort
        the array so that all elements before n are less than n, and all
        elements after n are greater than n
        """
        if len(nums) <= 1:
            return 0

        pivot = nums[-1]
        i = 0
        for j in range(len(nums)):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i = i+1
        nums[i], nums[-1] = nums[-1], nums[i]
        return i

    p = partition(nums)
    quick_sort(nums[:(p-1)])
    quick_sort(nums[p:])

def time_code():
    unsorted = [int(1000*random.random()) for i in xrange(1000000)]
    t0 = time.time()
    merge_sort(unsorted)
    t1 = time.time()
    t2 = time.time()
    insertion_sort(unsorted)
    t3 = time.time()
    print "Merge sort:     " + str(t1 - t0)
    print "Insertion sort: " + str(t3 - t2)


def main():
    unsorted = [int(1000*random.random()) for i in xrange(10000)]
    sorted_list = sorted(unsorted)
    print (sorted_list == bubble_sort(unsorted))
    print (sorted_list == insertion_sort(unsorted))


if __name__ == '__main__':
    # time_code()
    print "executed"
