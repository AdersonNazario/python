def é_hipotenusa(n) :
    a= 1
    b= 1
    r = False
    while a<=n :
        while b<=n :
            if n**2 == a**2 + b**2 :
                r = True
                break
            b+=1
        b= 1
        a+=1
    return r
        


def soma_hipotenusas(n) :
    s=0
    while n>=1 :
        if é_hipotenusa(n) :
            s+=n
        n-=1
    return s
