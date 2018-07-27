# Uses python3
import sys
import math

from priority_queue import PriorityQueue, MinBinaryHeap


BIG_DIST = 100000000.


def minimum_distance(x, y, n):
    # write your code here
    return prim(x, y, n)


def prim(x_points, y_points, n):
    """
    Implementation of Prim's algorithm for constructing
    a minimum spanning tree (MST) using priority queue (min binary heap).
    :param x_points: x coordinate list
    :param y_points: y coordinate list
    :param n: count of points
    :return: length of MST
    """
    cost = [(0, 0)]
    for i in range(1, n):
        cost.append((i, BIG_DIST))
    min_length = 0.
    # The priority queue is min binary heap.
    pqueue = PriorityQueue(cost)
    min_heap = MinBinaryHeap()
    while pqueue:
        min_weighted_vertex = min_heap.extract_min(pqueue)
        min_length += min_weighted_vertex[1]
        for i, p in enumerate(pqueue):
            # Calculation of the weight of the edge {v, u}
            # (the length of the segment between the points {x1, y1} and {x2, y2})
            edge_weight = math.sqrt((x_points[min_weighted_vertex[0]] - x_points[p[0]]) ** 2
                                    + (y_points[min_weighted_vertex[0]] - y_points[p[0]]) ** 2
                                    )
            if p[1] > edge_weight:
                min_heap.change_priority(pqueue, i, p[0], edge_weight)
    return min_length


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))
