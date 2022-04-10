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
    for i in range(N - M + 1): 
        j = 0

     
        while (j < M): 
            if (txt[i + j] != pat[j]): 
                break
            j += 1

        if (j == M): 
            list.append(i)

    return list





