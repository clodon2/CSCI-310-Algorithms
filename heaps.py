"""
Corey Verkouteren
12/2024
binary heap data structures, even structure left > right on last layer
min-heap min at top (children > parent), max-heap max at top (children < parent)
"""
class Heap:
    def __init__(self, array: list[int] = []):
        self.heap = array

    def get_parent(self, index: int):
        return index // 2

    def get_left(self, index: int):
        return 2 * index

    def get_right(self, index: int):
        return (2 * index) + 1

    def exchange(self, i1, i2):
        hold = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = hold


class MinHeap(Heap):
    def __init__(self, array: list[int] = False):
        super().__init__(array)

        if self.heap:
            self.build_min()

    def min_heapify(self, index):
        left = self.get_left(index)
        right = self.get_right(index)

        # if left child smaller, save as least -- if not save self (index)
        if (left < len(self.heap)) and (self.heap[left] < self.heap[index]):
            least = left
        else:
            least = index

        # if right child smaller, save as least
        if (right < len(self.heap)) and (self.heap[right] < self.heap[index]) and \
                (self.heap[left] > self.heap[right]):
            least = right

        # if we need to change structure, exchange and continue
        if least != index:
            self.exchange(index, least)
            self.min_heapify(least)

    def build_min(self, array: list[int] = False):
        """build min heap from array or re-build heap stored in self.heap"""
        if array:
            self.heap = array

        for i in range(len(self.heap) // 2, -1, -1):
            self.min_heapify(i)

    def insert(self, item: int):
        # store inserted value at bottom to start
        self.heap.append(item)
        last = len(self.heap) - 1
        parent = self.get_parent(last)

        # percolate inserted item up if parent larger
        while self.heap[parent] > item:
            # move parent node down to previous inserted node position
            self.heap[last] = self.heap[parent]
            # move to look at next highest node
            last = parent
            parent = self.get_parent(parent)

            # if at root, we have percolated to top
            if (last == 0) and (parent == 0):
                break

        # insert item in correct position
        self.heap[last] = item

    def extract_min(self):
        if not self.heap:
            return False

        min = self.heap[0]
        # remove last item and move to top
        last = self.heap.pop(len(self.heap) - 1)
        self.heap[0] = last
        # percolate down (fix structure)
        self.min_heapify(0)

        return min

    def decrease_key(self, index, new):
        if self.heap[index] < new:
            return False

        self.heap[index] = new
        parent = self.get_parent(index)

        # percolate up
        while index > 0 and self.heap[parent] > self.heap[index]:
            self.exchange(index, parent)
            index = self.get_parent(index)
            parent = self.get_parent(index)

    def increase_key(self, index, new):
        if self.heap[index] > new:
            return False

        self.heap[index] = new
        self.min_heapify(index)


class MaxHeap(Heap):
    def __init__(self, array: list[int] = False):
        super().__init__(array)

        if self.heap:
            self.build_max()

    def max_heapify(self, index):
        left = self.get_left(index)
        right = self.get_right(index)

        # if left is greater, save as highest -- else save current as highest
        if (left < len(self.heap)) and (self.heap[left] > self.heap[index]):
            most = left
        else:
            most = index

        # if right is greater, save as highest
        if (right < len(self.heap)) and (self.heap[right] > self.heap[index]) and \
                (self.heap[left] < self.heap[right]):
            most = right

        # if heap order needs to be changed, do so and continue
        if most != index:
            self.exchange(index, most)
            self.max_heapify(most)

    def build_max(self, array: list[int] = False):
        """build max heap from array or re-build heap stored in self.heap"""
        if array:
            self.heap = array

        for i in range(len(self.heap) // 2, -1, -1):
            self.max_heapify(i)

    def insert(self, item: int):
        # store inserted value at bottom to start
        self.heap.append(item)
        last = len(self.heap) - 1
        parent = self.get_parent(last)

        # percolate inserted item up if parent smaller
        while self.heap[parent] < item:
            # move parent node down to previous inserted node position
            self.heap[last] = self.heap[parent]
            # move to look at next highest node
            last = parent
            parent = self.get_parent(parent)

            # if at root, we have percolated to top
            if (last == 0) and (parent == 0):
                break

        # insert item in correct position
        self.heap[last] = item

    def extract_max(self):
        if not self.heap:
            return False

        min = self.heap[0]
        # remove last item and move to top
        last = self.heap.pop(len(self.heap) - 1)
        self.heap[0] = last
        # percolate down (fix structure)
        self.max_heapify(0)

        return min

    def increase_key(self, index, new):
        if self.heap[index] > new:
            return False

        self.heap[index] = new
        parent = self.get_parent(index)

        # percolate up
        while index > 0 and self.heap[parent] < self.heap[index]:
            self.exchange(index, parent)
            index = self.get_parent(index)
            parent = self.get_parent(index)

    def decrease_key(self, index, new):
        if self.heap[index] < new:
            return False

        self.heap[index] = new
        self.max_heapify(index)


if __name__ == "__main__":
    mh = MinHeap([5, 2, 3, 1, 6])
    print(mh.heap)

    mmh = MaxHeap([1, 5, 2, 3, 1, 6])
    print(mmh.heap)