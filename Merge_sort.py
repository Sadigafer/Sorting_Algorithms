# Merge sort

def sort_s(massive):
    if len(massive)<2:
        return massive[:]
    else:
        middle = int(len(massive)/2)
        left = sort_s(massive[:middle])
        right = sort_s(massive[middle:])
        return under_massives (left, right)

def under_massives (left, right):
    result = []
    i, j = 0, 0
    while i< len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=right[j:]+left[i:]
    return result