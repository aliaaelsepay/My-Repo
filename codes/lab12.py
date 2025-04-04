X= input("The number is :")
X=int(X)
list=[]

for i in range(1,X+1) : 
   array=[]
   for j in range(1,i+1) : 
        result=i*j
        array.append(result)

   list.append(array)
    

print(list)
"""
for i in range(len(list)):
    for j in range(len(list[i])):
        list[i][j]+=1
print(list)        
"""