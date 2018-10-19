
L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j+1] < L[j]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

print(bubble_sort(L))