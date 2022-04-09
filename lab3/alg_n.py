def search(pat, txt):
    list =[]
    M = len(pat)
    N = len(txt)
    if (len(pat) == 0 or len(txt) == 0):
        raise ValueError("Nothing was added to search")
    if (len(pat) == len(txt)):
        raise ValueError("Pattern lenght is equal to text lenght")
    if (len(pat) > len(txt)):
        raise ValueError("Lenght of string is bigger than the lenght of data ")
    for i in range(N - M + 1): #na kazda mozliwoa poczatkowa litere
        j = 0

     #jesli znajdziemy patern
        while (j < M): #patrzymy na fragment dlugosci patternu
            if (txt[i + j] != pat[j]): #jesli znaki sie roznia to znaczy ze nie to, wiec break
                break
            j += 1

        if (j == M): # jesli sie zgadza dlugosc przeszukana z dlugoscia paternu
            list.append(i)

    return list





