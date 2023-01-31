num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
sumdivisor =0
productdivisor =0
print("the common divisors of number",num1," and",num2," are-")
for i in range(1,min(num1,num2)+1):
    if num1%i==num2%1==0:
        sumdivisor=sumdivisor+1
        productdivisor=productdivisor*i
if(productdivisor%sumdivisor==0):
    print("yeah")
else:
    print("nah")
    
