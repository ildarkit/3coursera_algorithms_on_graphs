# Uses python3

import sys


def dfs(adj, used, order):
    # write your code here
    i = 0
    while True:
        while i < len(adj) and used[i]:
            i += 1
        if i < len(adj):
            explore(adj, used, v=i, post=order)
            i += 1
        else:
            break


def explore(adj, used, v=0, post=None):
    """
    Depth search in the graph
    :param adj: list of vertices with lists of adjacent vertices
    :param visited: list of visited vertices
    :param v: index of vertex
    :param post: list of postorder
    """
    used[v] = 1
    for w in adj[v]:
        if not used[w]:
            explore(adj, used, w, post)
    if post is not None:
        postvisit(v, post)


def postvisit(v, post):
    """
    Insert in postorder list
    :param v: index of vertex
    :param post: list of postorder vertices
    """
    post.insert(0, v)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    # write your code here
    dfs(adj, used, order)
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

