# Selection sort

def sort_vb (massive):
    for i in range (len(massive)):
        low = i
        for j in range (i+1, len(massive)):
            if massive[low] > massive[j]:
                low = j
        massive[low], massive[i]= massive[i], massive[low]
    return massive