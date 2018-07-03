#Uses python3

import sys


def acyclic(adj):
    visited = [0 for _ in range(len(adj))]
    post_visited = []
    explore(adj, visited, post=post_visited)
    result = False
    for v in post_visited:
        visited = [0 for _ in range(len(adj))]
        if not visited[v]:
            result = explore(adj, visited, v=v, check_cycle=True)
            if result:
                break
    return 1 if result else 0


def explore(adj, visited, v=0, post=None, check_cycle=False):
    visited[v] = 1
    result = False
    for w in adj[v]:
        if not visited[w]:
            result = explore(adj, visited, w, post, check_cycle)
            if result:
                break
        elif check_cycle:
            result = True
            break
    if post is not None:
        postvisit(v, post)

    return result


def postvisit(v, post):
    post.insert(0, v)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[1:(2 * m):2], data[0:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
