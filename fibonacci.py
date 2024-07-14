#fibonacci
n0=0
n1=1
print(n0,n1,end=" ")
def fibo(terms,n0,n1):
    if terms>0  :
        n2=n0+n1
        print(n2,end=" ")
        n0=n1
        n1=n2
        terms=terms-1
        fibo(terms,n0,n1)
fibo(10,n0,n1)