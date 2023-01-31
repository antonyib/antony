test_list=[1,5,3,6,3,5,6,1]
print("the original listis:"+str(test_list))
res=[]
for i in test_list:
     if i not in res:
       res.append(i)
