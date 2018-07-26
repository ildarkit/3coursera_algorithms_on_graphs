class PriorityQueue:

    def __init__(self, vertices):
        self.vertices = vertices

    def extract_min(self):
        """
        Get min element from root of heap.
        :return: tuple of vertex
        """
        result = self.vertices[0]
        self.vertices[0] = self.vertices[-1]
        self.vertices.pop()
        self.sift_down(0)
        return result

    def sift_down(self, i):
        size = len(self.vertices)
        min_index = i
        l = self.left_child(i)
        if l <= size - 1 and self.vertices[l][1] < self.vertices[min_index][1]:
            min_index = l
        r = self.right_child(i)
        if r <= size - 1 and self.vertices[r][1] < self.vertices[min_index][1]:
            min_index = r
        if i != min_index:
            self.vertices[i], self.vertices[min_index] = (self.vertices[min_index],
                                                          self.vertices[i])
            self.sift_down(min_index)

    def left_child(self, i):
        return i*2 + 1

    def right_child(self, i):
        return i*2 + 2

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, p):
        self.vertices.append(p)
        self.sift_up(len(self.vertices) - 1)

    def sift_up(self, i):
        while i > 0 and self.vertices[self.parent(i)][1] > self.vertices[i][1]:
            _parent = self.parent(i)
            self.vertices[_parent], self.vertices[i] = self.vertices[i], self.vertices[_parent]
            i = _parent

    def change_priority(self, i, *p):
        old = self.vertices[i]
        self.vertices[i] = p
        if old[1] > p[1]:
            self.sift_up(i)
        else:
            self.sift_down(i)
