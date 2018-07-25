from points import points_generator
from connecting_points import minimum_distance as kruskal
from connecting_points_prim import minimum_distance as prim


ERROR_THRESHOLD = 0.1


if __name__ == '__main__':
    stop = 1000
    total = 0
    err = 0
    while True:
        total += 1
        points = points_generator()
        if points is False:
            continue
        data = list(map(int, points.split()))
        n = data[0]
        x = data[1::2]
        y = data[2::2]
        res1 = kruskal(x, y, n)
        res2 = prim(x, y, n)
        if res1 != res2:
            err += 1
            print('res1 = {}, res2 = {}'.format(res1, res2))
            print(points)
        if total * ERROR_THRESHOLD <= err and err > 0 or total >= stop:
            break
        if total % 100 == 0:
            print('total = {}, err = {}'.format(total, err))