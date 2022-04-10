# - *- coding: utf- 8 - *-
from check_time import check_time

@check_time
def bubble_sort(lst):
    n = len(lst)
    for i in range(n): 
        for j in range(n-1): 
            if (lst[j]>lst[j+1]): 
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

