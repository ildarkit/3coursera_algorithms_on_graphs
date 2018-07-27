class BinaryHeap:

    @staticmethod
    def left_child(i):
        return i*2 + 1

    @staticmethod
    def right_child(i):
        return i*2 + 2

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    def insert(self, heap, p):
        heap.append(p)
        self.sift_up(heap, len(heap) - 1)

    def sift_up(self, *args):
        raise NotImplementedError

    def sift_down(self, *args):
        raise NotImplementedError

    def change_priority(self, *args):
        raise NotImplementedError


class MinBinaryHeap(BinaryHeap):
    """
    Minimum binary heap.
    """

    def extract_min(self, heap):
        """
        Get min element from root of heap.
        :return: tuple of vertex
        """
        result = heap.get_first_item()
        heap.swappop()
        self.sift_down(heap, 0)
        return result

    def sift_down(self, heap, i):
        size = len(heap)
        min_index = i
        left = self.left_child(i)
        if left <= size - 1 and heap[left] < heap[min_index]:
            min_index = left
        right = self.right_child(i)
        if right <= size - 1 and heap[right] < heap[min_index]:
            min_index = right
        if i != min_index:
            heap.swap(i, min_index)
            self.sift_down(heap, min_index)

    def sift_up(self, heap, i):
        while i > 0 and heap[self.parent(i)] > heap[i]:
            _parent = self.parent(i)
            heap.swap(_parent, i)
            i = _parent

    def change_priority(self, heap, i, vertex, weight):
        old = heap[i]
        heap[i] = (vertex, weight)
        if old > weight:
            self.sift_up(heap, i)
        else:
            self.sift_down(heap, i)


class PriorityQueue:

    def __init__(self, vertices):
        self.vertices = vertices

    def __getitem__(self, item):
        return self.vertices[item][1]

    def __setitem__(self, key, value):
        self.vertices[key] = value

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        self.iterator = iter(self.vertices)
        return self.iterator

    def __next__(self):
        return next(self.iterator)

    def get_first_item(self):
        return self.vertices[0]

    def swappop(self):
        self.vertices[0] = self.vertices[-1]
        self.vertices.pop()

    def swap(self, i, j):
        self.vertices[i], self.vertices[j] = self.vertices[j], self.vertices[i]

    def append(self, v):
        self.vertices.append(v)
