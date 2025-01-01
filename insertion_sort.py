"""
Corey Verkouteren
8/26/2024
Insertion Sort Algorithm (n**2)
"""
def insertion_sort(array):
    """
    sort an array by inserting the unsorted elements into their sorted spot individually
    :param array: an array of ints
    :return:
    """
    # start at one so that j isn't -1
    # (In this case the algorithm would still work, but only because python has circular lists)
    for i in range(1, len(array)):
        # key is sorted into the sorted side of the array
        key = array[i]
        # j becomes element before key in the array (the most recently sorted item)
        j = i - 1

        # if previous element in heap (j) is bigger than key
        while j > -1 and array[j] > key:
            # move the bigger element to right (j)
            array[j + 1] = array[j]
            # compare the next element to the left
            j = j - 1

        # once key is bigger than the element to the left, insert it in front
        # (remember that the element that was there was moved to the right)
        array[j + 1] = key

    return array
