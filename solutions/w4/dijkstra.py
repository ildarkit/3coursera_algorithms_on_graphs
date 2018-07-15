# Uses python3

import sys


BIG_DIST = 100000000


def distance(adj, cost, s, t):
    # write your code here
    return dijkstra(adj, cost, s, t)
    # return min_cost(s, t, prev, dist)


def dijkstra(adj, cost, s, t):
    dist = []
    # prev = []
    used = []
    for _ in range(len(adj)):
        dist.append(BIG_DIST)
        # prev.append(None)
        used.append(None)
    dist[s] = 0
    queue = [s]
    while queue:
        u = queue.pop()
        for i, v in enumerate(adj[u]):
            if used[v] is None:
                queue.insert(0, v)
                used[v] = v
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                # prev[v] = u
    return dist[t] if dist[t] != BIG_DIST else -1


# def min_cost(s, t, prev, dist):
#     result = 0
#     while s != t:
#         if t is not None:
#             if dist[t]:
#                 result += dist[t]
#         else:
#             return -1
#         t = prev[t]
#     return result


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
