X=input("The word is :")
V=['a','e','i','o','u']
count=0
for i in V :
 for j in X :
     if i==j :
        count +=1

print(count)