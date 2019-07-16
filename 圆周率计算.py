import random
import time


DARTS = 1000 * 1000
hits = 0.0
start = time.perf_counter()
for i in range(1, DARTS + 1):
    x, y = random.random(), random.random()
    res = pow(x ** 2 + y **2, 0.5)
    if res <= 1.0:
        hits += 1
pi = (4 * hits) / DARTS
print("圆周率的值是:{}".format(pi))
end = time.perf_counter()
print("计算时间为:{}".format(end - start))