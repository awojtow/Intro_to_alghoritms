def search(pat, txt, q):
    d = 256 
    list =[] 
    
    M = len(pat) 
    N = len(txt) 
    i = 0 
    j = 0 
    p = 0 
    t = 0 
    h = 1 
    if (len(pat) == 0 or len(txt) == 0):
        raise ValueError("Nothing was added to search")
    if (len(pat) == len(txt)):
        raise ValueError("Pattern lenght is equal to text lenght")
    if (len(pat) > len(txt)):
        raise ValueError("Lenght of string is bigger than the lenght of data ")
    
    for i in range(M-1):
        h = (h * d)% q 
    
    
    for i in range(M):
        p = (d * p + ord(pat[i]))% q 
        t = (d * t + ord(txt[i]))% q 

    for i in range(N-M + 1):
        
        
        
        if p == t:
            
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break 

            j+= 1 
            if j == M: 
                list.append(i)

        if i < N-M: 
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q 
            
            
            
            
            
            
            if t < 0:
                t = t + q
    return list


