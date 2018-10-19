
L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

def selection_sort(L):
    n = len(L)
    while n > 0:
        maxInd = 0
        for i in range(1, n):
            if L[i] > L[maxInd]: 
                maxInd = i
        tmp = L[n-1]
        L[n-1] = L[maxInd]
        L[maxInd] = tmp
        n -= 1
    return L

print(selection_sort(L))

