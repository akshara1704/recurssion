num=int(input("Enter any no to check whether it is primo or not="))
def primo(n,i,counter):
    if n==1:
        print("Prime hai 1 to")
    elif n%i==0 and n>i:
        print("Not prime")
    elif counter==n:
        print("prime")
    else:
        i=i+1
        counter=counter+1
        primo(n,i,counter)
primo(num,2,2)