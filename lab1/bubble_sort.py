# - *- coding: utf- 8 - *-
from check_time import check_time

@check_time
def bubble_sort(lst):
    n = len(lst)
    for i in range(n): #dla kazdego elemetu listy 
        for j in range(n-1): #dla kazdego następnego elementu 
            if (lst[j]>lst[j+1]): #jeśli nastepny element jest mniejszy - zamien miejscami 
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

