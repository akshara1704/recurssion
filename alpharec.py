def alpha(n):
    if n==90:
        return (chr(n))
    else:
        print(chr(n),end=" ")
        return alpha(n+1)
print(alpha(65))