n = int(input("Digite numero: "))
r = "não primo"
aux = n**(.5) +1
i=1
f = False
if (n==2 or n==3 or n==5 or n==7 or n==11 or n==13 or n==17 or n==19 or n==23) :
	r = "primo"
	f = True
if (n%2==0): f=True

while (i<=aux and not f) :
	i +=2
	if (n % i == 0): f = True
	if (n % i !=0 and n / i < i) :
		r="primo"
		f = True
print(r)
