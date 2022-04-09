# - *- coding: utf- 8 - *-
from check_time import check_time
import sys

sys.setrecursionlimit(100000)
#otrzymując pozycje startowa i końcowa oraz array, chcemy zwrocic index elementu
#który bedzie wskazywał na  pivota - czyli taki element który ma po swojej lewej stronie elementy mneijsze a po prawej - wieksze
#sa rozne wersje algorytmu (roznice sa w wyborze punktu podzialu) - mozna wybierac go losowo
#jako mediane, jako pierwszy albo ostatni element (tutaj zaimpelemtowany jest jako ostatni)
  
  
def partition(arr,low, high):
    i = (low-1)         # index ostatniego elementu mniejszego od pivota (takie ktory sie na razie udało znalezc)
    pivot = arr[high]     # ustalenie ostatniego elementu z zakresu jako pivota (zogdnei z ta wersja quicksorta)
  
    for j in range(low, high): #idziemy po calym okreslonym zakresie
        if arr[j] <= pivot: #jesli element jest mniejszy=pivotovi to zwieksz index najmniejszego elementu 
        #oraz zamien miejscami  
            i = i+1 #de facto zlicza ilosc elementów mniejszych od pivot 
            arr[i], arr[j] = arr[j], arr[i] #przerzucam na lewą strone rzeczy mniejsze od pivota 
  
    arr[i+1], arr[high] = arr[high], arr[i+1]  
    return (i+1) # tym miejscu powinien nastąpić podział - element o indexie i+1 dzieli array na elementy mniejsze i wieksze od siebie samego
  


  
@check_time
def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr #array 1 elementowy jest zawsze posortowany
    if low < high: #jeśli zakres nie jest zmkniety (warunek by poszła rekursja)

        pi = partition(arr, low, high) #wybranie miesca podziału
  
        quick_sort(arr, low, pi-1) #otrzymujemy dwie arraye - elementów mniejszych i wiekszych od pivota. 
        #bedziemy je sortowac oddzielnie, uzuwajac rekursji 
        quick_sort(arr, pi+1, high)
  
  