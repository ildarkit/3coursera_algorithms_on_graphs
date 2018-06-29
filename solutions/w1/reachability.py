#Uses python3

import sys


def reach(adj, x, y):
    # write your code here
    visited = [0 for _ in range(len(adj))]
    return 1 if explore(x, y, adj, visited) else 0


def explore(v, y, adj, visited):
    result = False
    visited[v] = 1
    if visited[y] == 1:
        return True
    for w in adj[v]:
        if not visited[w]:
            result = explore(w, y, adj, visited)
            if result:
                break
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
