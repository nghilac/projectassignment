def fibonacciFinder(max):
    i = 0
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j 
        j = k
        return("fibonacci found!")

def primeFinder(max):
    for i in range(2, max):
     for j in range(2,i):
        if i % j == 0:
          break 
    else: 
        print(i)
    return(max)
print(fibonacciFinder(100), primeFinder(15))
