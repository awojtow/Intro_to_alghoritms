# - *- coding: utf- 8 - *-
from check_time import check_time

@check_time
def selection_sort(lst):
    n = len(lst)
    for i in range(n): #dla kazdego elementu listy
        idx_min = i #ustal jako minimum dany element 
        for j in range(i+1,n): #dla wszystkich następnych elementów sprawdz 
            #czy nie sa przypadkiem mniejsze niz załoone minimum
            if lst[j]<lst[idx_min]: #porównaj 
                idx_min = j #jeśli którys z dalszych elemtnów jest mniejszy - ustal nowe minimym
        lst[i], lst[idx_min] = lst[idx_min], lst[i] #zamien mijscami elementy - minimum oraz dany elemetn tej pętli
    return lst 

