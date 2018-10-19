
L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

def partition(L, low, high):
    pivot = L[high]
    i = low - 1
    for j in range(low, high):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i+1]
    return i+1

def quick_sort(L, low=0, high=len(L)-1):
    if low < high:
        pi = partition(L, low, high) # partition index
        quick_sort(L, low, pi - 1)
        quick_sort(L, pi+1, high)
    return L

print(quick_sort(L))