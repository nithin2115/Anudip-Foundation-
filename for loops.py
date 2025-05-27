# Loops: Even and Odd numbers 
a=[2,3,4,5,6]
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],"is even number")
    else:
        print(a[i] ," is odd number")
print()

# numbers printing  using while loop
i=1
while i<10:
    print(i)
    i+=1
    
# Array elements is divisble by 10 or not
a=[1,3,5,10,50]
for i in range(len(a)):
    if (a[i]%10==0):
        print(a[i],"is divisble by 10")
    else:
        print(a[i],"is not divisble by 10")
print()

# vowels or not present in string
str="AnudipA"
b=str.lower()
c='a,e,i,o,u'
for i in b:
    if i in c:
        print(i,b.count(i),"is present in b")
    else:
        print(i,b.count(i), "is not in b")
