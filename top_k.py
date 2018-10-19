import random, math

L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36]
# L = [6, 5, 4, 5]
# L = [1, 2, 3]

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller.append(val)
        if val > v: bigger.append(val)
    return (smaller, [v], bigger)

def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, _, right) = partition(L, v)
    if len(left) == k: return left
    if len(left)+1 == k: return left+[v]
    if len(left) > k: return top_k(left, k)
    return left + [v] + top_k(right, k-len(left)-1)

print(top_k(L, 6))

# median is the number that minimizes the sum of the absolute difference
def find_median(L):
    # return max(top_k(L, math.ceil(len(L)/2.0))) # for python2 to work
    return max(top_k(L, math.ceil(len(L)/2)))

print(find_median(L))
print()
print(sorted(L))