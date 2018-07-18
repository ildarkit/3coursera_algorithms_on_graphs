from gen_graph import generate_simple_graph
from dijkstra import dijkstra_list, naive_distance


ERROR_THRESHOLD = 0.1


if __name__ == '__main__':
    stop = 1000
    total = 0
    err = 0
    while True:
        total += 1
        graph = generate_simple_graph()
        if graph is False:
            continue
        data = list(map(int, graph.split()))
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
        res1 = dijkstra_list(adj, cost, s, t)
        res2 = naive_distance(adj, cost, s, t)
        if res1 != res2:
            err += 1
            print('res1 = {}, res2 = {}'.format(res1, res2))
            print(graph)
        if total * ERROR_THRESHOLD <= err and err > 0 or total >= stop:
            break
        if total % 100 == 0:
            print('total = {}, err = {}'.format(total, err))

