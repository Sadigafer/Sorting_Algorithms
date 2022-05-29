import time
import numpy as np
from Selection_sort import sort_vb as Selection_sort
from Bubble_Sorting import sort_p as Bubble_Sorting
from Insertion_sort import sort_vs as Insertion_sort
from Merge_sort import sort_s as Merge_sort
from Quick_sort import sort_b as Quick_sort

# Speed check
np.random.seed(1)
massive = np.random.randint(0, high=1000, size=200)

start_1 = time.perf_counter()
Selection_sort(massive.copy())
finish_1_start_2 = time.perf_counter()
Bubble_Sorting(massive.copy())
finish_2_start_3 = time.perf_counter()
Insertion_sort(massive.copy())
finish_3_start_4 = time.perf_counter()
Merge_sort(massive.copy())
finish_4_start_5 = time.perf_counter()
Quick_sort(massive.copy())
finish_5 = time.perf_counter()


print(f"Selection sort: {finish_1_start_2-start_1:0.3f} seconds")
print(f"Bubble Sorting: {finish_2_start_3-finish_1_start_2:0.3f} seconds")
print(f"Insertion sort: {finish_3_start_4-finish_2_start_3:0.3f} seconds")
print(f"Merge sort: {finish_4_start_5-finish_3_start_4:0.3f} seconds")
print(f"Quick sort: {finish_5-finish_4_start_5:0.3f} seconds")