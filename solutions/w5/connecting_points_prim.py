# Uses python3
import sys
import math


BIG_DIST = 100000000.


def minimum_distance(x, y, n):
    # write your code here
    return prim(x, y, n)


def prim(x_points, y_points, n):
    """
    Implementation of Prim's algorithm for constructing
    a minimum spanning tree (MST) using priority queue.
    :param x_points: x coordinate list
    :param y_points: y coordinate list
    :param n: count of points
    :return: length of MST
    """
    cost = []
    adj = []
    for i in range(n):
        cost.append(BIG_DIST)
        adj.append(i)
    adj = set(adj)
    i = 0
    cost[i] = 0
    min_length = 0.
    # The priority queue is just a list in this case.
    pqueue = [i]
    while pqueue:
        v = pqueue.pop(0)
        min_length += cost[v]
        min_cost = BIG_DIST
        vertex_min_cost = -1
        for u in adj:
            if u != v:
                # Calculation of the weight of the edge {v, u}
                # (the length of the segment between the points {x1, y1} and {x2, y2})
                edge_weight = math.sqrt((x_points[v] - x_points[u]) ** 2
                                        + (y_points[v] - y_points[u]) ** 2
                                        )
                if cost[u] > edge_weight:
                    cost[u] = edge_weight
                # Save the vertex number with minimum weight
                if min_cost > edge_weight:
                    min_cost = edge_weight
                    vertex_min_cost = u
        if vertex_min_cost != -1:
            # Adding a vertex with minimal weights to the queue.
            # A queue always contains one vertex.
            pqueue.append(vertex_min_cost)
        # Removing a vertex v from all lists of adjacent vertices,
        # because weights from this vertex to all others are already known.
        # At the next iteration, the weight of the {v, u} edge will be summed with min_length.
        adj = adj ^ {v}
    return min_length


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))
