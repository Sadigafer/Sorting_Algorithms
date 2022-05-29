# Bubble Sorting

def sort_p (massive):
    swap = True
    while swap:
        swap = False
        for i in range (len(massive)-1):
            if massive[i]>massive[i+1]:
                massive[i], massive[i+1] = massive[i+1], massive[i]
                swap = True
    return massive