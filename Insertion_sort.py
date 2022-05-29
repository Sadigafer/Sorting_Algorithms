# Insertion sort

def sort_vs (massive):
    for i in range (1, len(massive)):
        current = massive[i]
        j = i-1
        while (j>=0) and current < massive [j]:
            massive [j+1] = massive [j]
            j = j-1
        massive [j+1] = current
    return massive