
L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

def merge_sort(L):
    result = []
    if len(L) < 2: return L
    mid = len(L)//2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort(L))