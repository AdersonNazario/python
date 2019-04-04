def ehPrimo (n) :
    r = False
    aux = n**(.5) +1
    i=1
    f = False
    if (n==2 or n==3 or n==5 or n==7 or n==11 or n==13 or n==17 or n==19 or n==23) :
        r = True
        f = True
    if (n%2==0): f=True

    while (i<=aux and not f) :
        i +=2
        if (n % i == 0): f = True
        if (n % i !=0 and n / i < i) :
            r=True
            f = True
    return r


def n_primos(n) :
    s=0
    while n >=2 :
        if ehPrimo(n) :
            s+=1
        n-=1
    return s
