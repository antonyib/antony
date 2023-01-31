l=[]
n=int(input("enter number of elements:"))
for i in range(n):
    e=int(input("enter an elements:"))
    l.append(e)
print("the original list is",1)
odd=0
even=0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("the number of odd numbers in the list are",odd)
print("the number of even numbers in the list are",even)
        
