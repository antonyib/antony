l=[]
n=int(input("enter number of elements:"))
for i in range(n):
    e=int(input("enter an elements:"))
    l.append(e)
print("the original list is",l)
s=0
for i in l:
   s=s+i
print("the sum of all integers present in", 1," is",s)   
