a=[]
n=int(input("enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("enter element"+str(x+1)+":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("new list is:")
print(a)
