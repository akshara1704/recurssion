def factorial(n):
    if n==1:
        return n
    else:
        a=factorial(n-1)
        return (n*a)
print(factorial(5))