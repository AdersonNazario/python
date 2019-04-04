def ePrimo(n) :
    aux = n**(.5) +1
    i=1
    f = False
    r = False
    if (n==2 or n==3 or n==5 or n==7 or n==11 or n==13 or n==17 or n==19 or n==23) :
            f = True
            r = True
    if (n%2==0): f=True

    while (i<=aux and not f) :
            i +=2
            if (n % i == 0): f = True
            if (n % i !=0 and n / i < i) :
                    r= True
                    f = True
    return r

def maior_primo (x) :
    for i in range(x,1,-1):
        if ePrimo(i) :
            return i
    return 0
        
