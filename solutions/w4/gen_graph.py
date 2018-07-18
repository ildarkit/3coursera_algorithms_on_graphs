import time
import random


MAX_VERTICES = 16
MAX_EDGES = 31
MAX_WEIGHTS = 11


def generate_simple_graph():
    vertices = random.randint(5, MAX_VERTICES)
    edges = random.randint(0, MAX_EDGES)
    edges_buf = dict()
    gr = [vertices, edges]
    start = int(time.time())
    for _ in range(edges):
        u = random.randint(1, vertices)
        v = u
        while v == u:
            if int(time.time()) - start > 3:
                return False
            v = random.randint(1, vertices)
        w = random.randint(0, MAX_WEIGHTS)
        while (u, v) in edges_buf:
            u = random.randint(1, vertices)
            v = u
            while v == u:
                if int(time.time()) - start > 3:
                    return False
                v = random.randint(1, vertices)
        edges_buf[(u, v)] = w
        gr.append(u)
        gr.append(v)
        gr.append(w)
    a = random.randint(1, vertices)
    b = a
    while b == a:
        if int(time.time()) - start > 3:
            return False
        b = random.randint(1, vertices)
    gr.append(a)
    gr.append(b)
    return ' '.join(map(str, gr))


if __name__ == '__main__':
    graph = generate_simple_graph()
    print(graph)

