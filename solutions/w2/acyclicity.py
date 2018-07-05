#Uses python3

import sys


def acyclic(adj, reversed_adj):
    """
    The function of finding cycles in a directed graph, i.e. SCC
    :param adj: list of vertices with lists of adjacent vertices
    :param reversed_adj: list of vertices with lists of adjacent vertices
           of reversed graph
    :return: 0 if cycle is not found, else 1
    """
    visited = [0 for _ in range(len(adj))]
    post_visited = []
    dfs(reversed_adj, visited, post_visited)
    visited = [0 for _ in range(len(adj))]
    for v in post_visited:
        if not visited[v] and explore(adj, visited, v=v) > 1:
            return 1
    return 0


def dfs(adj, visited, post_visited):
    """
    Traverse all vertices in the graph
    :param adj: list of vertices with lists of adjacent vertices
    :param visited: list of visited vertices
    :param post_visited: list of postorder
    """
    i = 0
    while True:
        while i < len(adj) and visited[i]:
            i += 1
        if i < len(adj):
            explore(adj, visited, v=i, post=post_visited)
            i += 1
        else:
            break


def explore(adj, visited, count=0, v=0, post=None):
    """
    Depth search in the graph
    :param adj: list of vertices with lists of adjacent vertices
    :param visited: list of visited vertices
    :param count: the number of vertices in strongly connected components
    :param v: index of vertex
    :param post: list of postorder
    :return: count
    """
    visited[v] = 1
    count += 1
    for w in adj[v]:
        if not visited[w]:
            count = explore(adj, visited, count, w, post)
    if post is not None:
        postvisit(v, post)
    return count


def postvisit(v, post):
    """
    Insert in postorder list
    :param v: index of vertex
    :param post: list of postorder vertices
    """
    post.insert(0, v)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    reversed_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        reversed_adj[b - 1].append(a - 1)
    print(acyclic(adj, reversed_adj))
