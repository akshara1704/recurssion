'''
 Write a program with recursion to print the multiple of user inputted number
 between 10 and 80 should not be included

'''
a=int(input())
count=0
def multi(a,i,count):
    if i<80:
        if i%a == 0:
            print(i,end=" ")

        i=i+1
        multi(a,i,count+1)
multi(a,11,0)
print("\nThere are only",count,"multiples of",a)

