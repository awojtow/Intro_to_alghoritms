def search(pat, txt, q):
    d = 256 ## dlugosc alfabetu - lisc liter
    list =[] ## stworzona przez nas lita
    #q to liczba pierwsza
    M = len(pat) ## dlugosc paternu
    N = len(txt) ## dlugosc calego tekstu
    i = 0 ##
    j = 0 ##
    p = 0 # wartosc funkcji skrotu dla paternu
    t = 0 # wartosc funkcji skrotu dla paternu
    h = 1 ## wartosc do liczenia najwiekszej potegi - potem uzywany w odejmowaniu
    if (len(pat) == 0 or len(txt) == 0):
        raise ValueError("Nothing was added to search")
    if (len(pat) == len(txt)):
        raise ValueError("Pattern lenght is equal to text lenght")
    if (len(pat) > len(txt)):
        raise ValueError("Lenght of string is bigger than the lenght of data ")
    ## obluga bledow zgodna z zadaniem
    for i in range(M-1):
        h = (h * d)% q #koncowo uzyskamy w tymprzypadku 256^(dlugosc pat) %q
    ##liczenie najwiekszej potegi dla danej dlugosci paternu zeby potem to odejmowac przy aktualizacji!
    ## policz funkcje skrotu paternu oraz pierwszego okna ! dlatego M
    for i in range(M):
        p = (d * p + ord(pat[i]))% q # funcja skrotu paternu 
        t = (d * t + ord(txt[i]))% q # f. skrotu pierwszego framgentu tekstu (okna)

    for i in range(N-M + 1):
        # dzielimy tekst na okna i sprawdzamy kazde okno
        # czy zgadza się z oknem naszego paternu
        # jesli sie zgadza to :
        if p == t:
            #sprawdzamy czy na pewno sie to zgadza (tzn czy kazda litera sie zgadza)
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break ## jesli nie to break

            j+= 1 ## dodajemy bo range jest do M
            if j == M: ## a jesli odpowiednia dlugosc jest sprawdzona tak to dodajemy do listy
                list.append(i)

        if i < N-M: ## updatujemy funkcje skrotu  zgodnie ze wzorem :
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q 
            # usuwamy tutaj największy "bit" a reszte musimy pomnożyć *d
            #podobnie do operacji na bitach, w ktorych usuwamy najbardziej znaczacy
            #a resztea jest mnozona o nasze d po to, zeby powstal nowy najbardziej znaczacy
            #tego samego typu --> i dodajemy na koncu do tego najmniej znaczacy bit czyli
            #ord(txt[i+M])
            #istnieje prawdopodobienstwo, ze bedziemy mieli wartosc ujemna (zalezy to od dluosci alfabetu, paternu itp)
            if t < 0:
                t = t + q
    return list
# Driver program to test the above function

