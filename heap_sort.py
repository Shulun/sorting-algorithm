#
# Implement heap_sort 
#

def remove_min(L):
    del L[0]
    if L: L.insert(0, L[-1])
    else: return []
    del L[-1]
    down_heapify(L, 0)
    return L

def root(i):
    return i==0
def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children
def down_heapify(L, i):
    # If i is a leaf, heap property holds
    if is_leaf(L, i): 
        return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        return
    # If i has two children...
    # check heap property
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]: 
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left_child(i)] < L[right_child(i)]:
        # Swap into left child
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i))
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i))
        return

#########
# Testing Code
#

# build_heap
def build_heap(L):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
    return L

def test():
    L = range(10)
    build_heap(L)
    remove_min(L)
    # now, the new minimum should be 1
    assert L[0] == 1

# L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]
# print('original :', L)
# print()
# build_heap(L)
# print('heapified :', L)
# print()
# remove_min(L)
# print('removed min :', L)

L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

def heap_sort(L):
    retLst = []
    build_heap(L)
    while len(L) > 0:
        retLst.append(L[0])
        remove_min(L)
    return retLst

sortedLst = heap_sort(L)
print(sortedLst)
