import random

# Quick sort

def sort_b(massive):
    if len(massive)<=1:
        return massive
    else:
        x=random.choice(massive)
        left = []
        right = []
        middle = []
        for n in massive:
            if n<x:
                left.append(n)
            elif n> x:
                right.append(n)
            else:
                middle. append(n)
        return sort_b(left) + middle + sort_b(right)