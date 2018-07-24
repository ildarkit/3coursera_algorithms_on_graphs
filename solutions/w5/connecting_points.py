# Uses python3
import sys
import math


def minimum_distance(x, y, n):
    # write your code here
    edges = build_graph(x, y, n)
    return kruskal(edges, n)


def build_graph(x_points, y_points, n):
    """
    Creating a weighted connected undirected graph
    with all edges between all vertices.
    :param x_points: x coordinate list
    :param y_points: y coordinate list
    :return: list of weighted edges
    """
    edges = []
    for i in range(n - 1):
        j = i + 1
        while j < n:
            weight = math.sqrt((x_points[i] - x_points[j])**2
                               + (y_points[i] - y_points[j])**2
                               )
            edges.append((i, j, weight))
            j += 1
    return edges


def kruskal(edges, len_vertices):
    """
    Implementation of Kruskal's algorithm for constructing
    a  minimum spanning tree (MST) using disjoint sets.
    :param edges: list of weighted edges
    :param len_vertices: count of vertices
    :return: length of MST
    """
    min_lenght = 0.
    disjoint_set = []
    linked = []
    # Initialization of disjoint sets
    # and an auxiliary list of disjoint sets
    # representing the same object in a Python.
    # The set is wrapped with a list,
    # by means of which all the elements
    # of the same list are updated in disjoint_set
    # (due to the mutable property of lists in Python).
    for i in range(len_vertices):
        disjoint_set.append([{i}])
        linked.append(False)
    # sorting edges in non-decreasing weight order
    edges = sorted(edges, key=lambda edge: edge[2])
    for v, u, w in edges:
        if not disjoint_set[v][0] is disjoint_set[u][0]:
            # Vertices v and u are in different disjoint sets.
            # Sum the weight of an edge between vertices v and u
            min_lenght += w
            # union of sets
            disjoint_set[v][0].update(disjoint_set[u][0])
            if linked[u]:
                # The element in the index u (the list in this case)
                # is the same object in some other index,
                # so only the content of the list is updated.
                disjoint_set[u][0] = disjoint_set[v][0]
            else:
                # In disjoint_set[u], a list of disjoint_set[v] is written.
                # Thus, when accessing different elements of the disjoint_set list,
                # the same object is accessed (list) with the union set inside.
                disjoint_set[u] = disjoint_set[v]
                # Flags are set that these elements represent
                # the same set (the same object in Python)
                linked[u] = linked[v] = True
    return min_lenght


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))
