
L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and key < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key
    return L
print(insertion_sort(L))

# For sorting the top k: theta(nk), only go through k items in the for loop