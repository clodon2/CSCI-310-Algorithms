"""
Corey Verkouteren
8/28/24
Merge Sort Algorithm (nlogn) split array, sort while merging, recursion
"""
def merge_sort(array, start, end):
    # if array is empty or one element, end recursion (list is sorted/smallest)
    if start >= end:
        return

    # get midpoint of list
    mid = (start + end) // 2

    # divide left side of list
    merge_sort(array, start, mid)
    # divide right side of list
    merge_sort(array, mid + 1, end)

    # sort each side of the new split array
    merge(array, start, mid, end)


def merge(array, start, mid, end):
    # get lengths of left and right arrays
    l_length = mid - start
    r_length = end - mid

    # create left and right arrays
    l_array = array[start:mid]
    r_array = array[mid:(end + 1)]

    # used to iterate through arrays, l is for left, r for right, k for original
    l = 0
    r = 0
    k = start

    # debugging print
    print(l, l_length, l_array, r, r_length, r_array, "    ", array, start, mid, end)
    # while within bounds of both lists
    while l < l_length and r < r_length:
        # if element in left array is bigger, sort it into the original array in current subarray position
        if l_array[l] <= r_array[r]:
            array[k] = l_array[l]
            l += 1
        # if element in right array is bigger, sort it into the original array in current subarray position
        else:
            array[k] = r_array[r]
            r += 1
        k += 1

    # if there are still elements unsorted in left array, append to end of sorted
    while l < l_length:
        array[k] = l_array[l]
        l += 1
        k += 1

    # if there are still elements unsorted in right array, append to end of sorted
    while r < r_length:
        array[k] = r_array[r]
        r += 1
        k += 1

    # debugging print for final sorted subarray
    print(array)


test = [8, 2, 3, 4, 10, 6, 7, 8, 9]

merge_sort(test, 0, 9)

print(test)

