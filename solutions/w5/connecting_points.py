# Uses python3
import sys
import math


def minimum_distance(x, y):
    # write your code here
    edges = build_graph(x, y)
    return kruskal(edges, len(x))


def build_graph(x_points, y_points):
    edges = []
    for i in range(len(x_points) - 1):
        j = i + 1
        while j < len(x_points):
            weight = math.sqrt(abs(x_points[i] - x_points[j])**2
                               + abs(y_points[i] - y_points[j])**2
                               )
            edges.append((i, j, weight))
            j += 1
    return edges


def kruskal(edges, len_vertices):
    min_lenght = 0.
    disjoint_set = []
    for i in range(len_vertices):
        disjoint_set.append({i})
    edges = sorted(edges, key=lambda edge: edge[2])
    for v, u, w in edges:
        if disjoint_set[v] and disjoint_set[u] and u not in disjoint_set[v] and v not in disjoint_set[u]:
            min_lenght += w
            disjoint_set[v] = disjoint_set[v].union(disjoint_set[u])
            disjoint_set[u] = set()
    return min_lenght


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
