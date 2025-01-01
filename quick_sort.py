"""
Corey Verkouteren
12/2024
Quick Sort Algorithm Θ(nlogn) expected
"""
def quick_sort(array: list[int], start: int = 0, end: int = 0):
    # default to sort whole heap
    if not end:
        end = len(array) - 1

    # stop sorting when partition has no elements
    if start < end:
        # get middle of array
        mid = qs_partition(array, start, end)
        # sort partitions based on middle
        quick_sort(array, start, mid - 1)
        quick_sort(array, mid + 1, end)


def qs_partition(array: list[int], start: int, end: int):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            # if element less, move to low side of partition
            # and move higher to high end
            exchange(array, i, j)

    # put [ivot in correct spot (between low and high)
    exchange(array, i + 1, end)
    return i + 1


def exchange(array: list, index1: int, index2: int):
    hold = array[index1]
    array[index1] = array[index2]
    array[index2] = hold


if __name__ == "__main__":
    test_array = [2, 8, 7, 1, 3, 5, 6, 4]
    print("%-8s" % "unsorted", test_array)
    quick_sort(test_array)
    print("%-8s" % "sorted", test_array)