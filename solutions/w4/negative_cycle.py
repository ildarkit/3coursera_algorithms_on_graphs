# Uses python3

import sys


BIG_DIST = 100000000


def negative_cycle(adj, cost):
    # write your code here
    return bellman_ford(adj, cost)


def bellman_ford(adj, cost):
    """
    Implementation of the Bellman-Ford algorithm
    for searching of negative cycles.
    To do this, need to perform relaxing a k-times for all vertices.
    There is the negative cycle in the graph
    if the change of dist occurs at the last iteration.

    :param adj: list of lists of adjacency vertices
    :param cost: list of lists of weight
    :return: 1 if there is negative cycles, otherwise return 0
    """
    dist = [BIG_DIST for _ in range(len(adj))]
    dist[0] = 0
    k = 1
    while k <= len(adj):
        is_changed = False
        for u in range(len(adj)):
            for i, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][i]:
                    is_changed = True
                    if k == len(adj):
                        return 1
                    dist[v] = dist[u] + cost[u][i]
        if not is_changed:
            return 0
        k += 1


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
    print(negative_cycle(adj, cost))
