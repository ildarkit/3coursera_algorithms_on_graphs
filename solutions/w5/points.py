import time
import random


NPOINTS = 5
MIN_POINT = 0
MAX_POINT = 4


def points_generator():
    vertices = random.randint(1, NPOINTS)
    points = set()
    result = [vertices]
    start = int(time.time())
    for _ in range(vertices):
        x = random.randint(MIN_POINT, MAX_POINT)
        y = random.randint(MIN_POINT, MAX_POINT)
        p = (x, y)
        while p in points:
            if int(time.time()) - start > 3:
                return False
            x = random.randint(MIN_POINT, MAX_POINT)
            y = random.randint(MIN_POINT, MAX_POINT)
            p = (x, y)
        result.extend(p)
    return ' '.join(map(str, result))