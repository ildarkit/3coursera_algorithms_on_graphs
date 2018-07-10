# Uses python3

import sys


BIG_DIST = 100000000


def distance(adj, s, t):
    # write your code here
    prev = bfs(adj, s)
    spath = path(s, t, prev)
    return spath


def bfs(adj, s):
    dist = []
    prev = []
    for _ in range(len(adj)):
        dist.append(BIG_DIST)
        prev.append(None)
    dist[s] = 0
    queue = []
    queue.insert(0, s)
    while queue:
        u = queue.pop()
        for v in adj[u]:
            if dist[v] == BIG_DIST:
                queue.insert(0, v)
                dist[v] = dist[u] + 1
                prev[v] = u
    return prev


def path(s, t, prev):
    result = []
    while s != t:
        if t is not None:
            result.append(t)
        else:
            return -1
        t = prev[t]
    return len(result)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
