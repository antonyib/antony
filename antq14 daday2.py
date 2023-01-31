a=[]
n=int(input("enter the number of element in list:"))
for x in range(0,n):
    element=int(input("enter element"+str(x+1)+ ":"))
    a.append(element)
b=set()
unique=[]
for x in a:
   if x not in b:
       unique.append(x)
       b.add(x)
       print("non depulicate item:")
       print(unique)                                   
