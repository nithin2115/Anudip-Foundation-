# (List,Dict,Tuple) Program
a=[1,2,3,4,5]
c=a[0]
print(c)

# Count of elements in list
a=[1,2,1,4,6,3,5]
for i in a:
    b=a.count(i)
    print("num :",i, "count:" ,b)
    
#  dict
a={"name":'nithin',"age":21}
c=a["name"]
print(c)

# Sum() and max() and min()
a=[1,2,3,4,5]
c=max(a)
print(c)
d=min(a)
print(d)
e=sum(a)
print(e)
