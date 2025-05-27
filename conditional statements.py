# conditional statements : vote program
age=int(input())
name=input()
if age>=18:
    print(f"{name} age is {age} eligible for voting")
else:
    print(f"{name} is not eligible  for voting")

# using the break statement in if else syntax
a=[1,2,3,4,5]
n=len(a)
for i in range(len(a)):
    if (a[i]%n)==0:
        print(a[i])
        break
    else:
        pass
