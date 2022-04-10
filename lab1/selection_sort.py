# - *- coding: utf- 8 - *-
from check_time import check_time

@check_time
def selection_sort(lst):
    n = len(lst)
    for i in range(n): 
        idx_min = i 
        for j in range(i+1,n): 
           
            if lst[j]<lst[idx_min]: 
                idx_min = j 
        lst[i], lst[idx_min] = lst[idx_min], lst[i] 
    return lst 

