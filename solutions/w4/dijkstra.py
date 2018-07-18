# Uses python3

import sys


BIG_DIST = 100000000
USED_DIST = 1000000000


def distance(adj, cost, s, t):
    # write your code here
    return dijkstra_list(adj, cost, s, t)


def dijkstra_list(adj, cost, s, t):
    """
    Implementation of Dijkstra's algorithm for finding the path
    with the least cost of flight. For this, a list of distances was used
    (the asymptotics of O (V ** 2)).
    :param adj: list of adjacency
    :param cost: list of costs of adjacency nodes
    :param s: start node
    :param t: end node
    :return: distance of end node
    """
    dist = []
    for i in range(len(adj)):
        dist.append(BIG_DIST)
    dist[s] = 0
    len_queue = len(adj)
    dist2 = dist[:]
    while len_queue:
        # get node with min distance
        u = dist2.index(min(dist2))
        len_queue -= 1
        dist2[u] = USED_DIST
        for i, v in enumerate(adj[u]):
            # relaxing
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                dist2[v] = dist[v]
    return dist[t] if dist[t] != BIG_DIST else -1


def naive_distance(adj, cost, s, t):
    """
    A naive realization of finding a path with
    a minimum cost of a flight.
    Calculations will occur as long as the distance varies.
    :param adj: list of adjacency
    :param cost: list of costs of adjacency nodes
    :param s: start node
    :param t: end node
    :return: distance of end node
    """
    dist = [BIG_DIST for _ in range(len(adj))]
    dist[s] = 0
    i = s
    is_changed = False
    while True:
        u = adj[i]
        for j, v in enumerate(u):
            if dist[v] > dist[i] + cost[i][j]:
                is_changed = True
                dist[v] = dist[i] + cost[i][j]
        i += 1
        if i == len(adj):
            if is_changed:
                i = 0
                is_changed = False
            else:
                break
    return dist[t] if dist[t] != BIG_DIST else -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
    # print(naive_distance(adj, cost, s, t))
