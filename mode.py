#
# Given a list L of n numbers, find the mode 
# (the number that appears the most times).  
# Your algorithm should run in Theta(n).
# If there are ties - just pick one value to return 
#
from operator import itemgetter
import random

# def mode(L):
#     # your code here
#     d = {}
#     maxCount = 0
#     track = []
#     for val in L:
#         d[val] = d.get(val, 0) + 1
#         if d[val] > maxCount:
#             maxCount = d[val]
#     for k, v in d.items():
#         if v == maxCount: track.append(k)
#     return track[random.randrange(len(track))]

def mode1(L):
    # your code here
    d = {}
    maxCount = 0
    track = []
    for val in L:
        d[val] = d.get(val, 0) + 1
        if d[val] > maxCount:
            maxCount = d[val]
            mostVal = val
    return mostVal

from collections import defaultdict
def mode(L):
    counts = defaultdict(int)
    for v in L:
        counts[v] += 1
    return max(counts, key = lambda x: counts[x])

def mode2(L):
    return max(set(L), key = lambda x: L.count(x))

####
# Test
#
import time
from random import randint

def test():
    assert 5 == mode([1, 5, 2, 5, 3, 5])
    iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
    times = []
    for i in iterations:
        L = []
        for _ in range(i):
            L.append(randint(1, 10))
        start = time.clock()
        for _ in range(500):
            mode(L)
        end = time.clock()
        print(start, end)
        times.append(float(end - start))
    slopes = []
    for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
        print((x1, x2), (y1, y2))
        slopes.append((y2 - y1) / (x2 - x1))
    # if mode runs in linear time, 
    # these factors should be close (kind of)
    print(slopes)

test()
                # 