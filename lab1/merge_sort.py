# - *- coding: utf- 8 - *-
from check_time import check_time

@check_time
def merge_sort(myList):
    if len(myList) > 1:
        # Wyznaczanie połowy tablicy i stworzenie dwóch osobnych list
        # po lewej i prawej stronie względem wyznaczonej połowy
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Rekursja dla wyznaczonych wyżej połów
        # (jeżeli wyznaczone listy left/right mają tylko jeden element
        # rekursja się zatrzymuje)
        merge_sort(left)
        merge_sort(right)

        # Wywołane wyżej mergeSorty prawej i lewej strony dają nam 
        # rekurencyjnie ustawione elementy w tych tablicach

        # Inicjacja iteratorów dla połów
        i = 0
        j = 0
        
        # Inicjacja iteratora dla głównej listy
        k = 0
        
        # Porównujemy kolejne (odpowiadające) wartości w stworzonych listach:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # Jeżeli element z lewej listy jest mniejszy od tego z prawej listy
              # zostaje on dodany na początek głównej listy
              myList[k] = left[i]
              # Zwiększamy iterator z lewej listy
              i += 1
            else:
                # jeżeli element prawej listy jest mniejszy
                # wtedy on przechodzi do listy głównej
                # i przechodzimy do kolejnego elementu prawej listy
                myList[k] = right[j]
                j += 1
            # Przechodzimy do kolejnego "miejsca" w głównej tablicy
            k += 1

        # Kiedy w liście prawej lub lewej zostaną wartości nieuporządkowane
        # tj. kiedy elementy jednej listy zostały wstawione do głównej listy
        # a w drugiej jeszcze zostały, bo były "większe" od tych z pierwszej listy
        # wtedy zostają one kolejne dodane do głównej listy
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
            
