dic={}
def dicta(length):
    if length>0:
        a=input("enter key= ")
        b=input("enter value=")
        dic[a]=b
        dicta(length-1)
l=int(input("enter length of dictionary= "))
dicta(l)
print(dic)