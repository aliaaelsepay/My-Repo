numberss=[]

for i in range(0,5):
    numbers=input("Enter array: ")
    if not numbers.isdigit():
        numbers =input("Enter a valid number: ")
    
    else:
     numberss.append(numbers)
 
desd=sorted(numberss,reverse=True) 
aesd=sorted(numberss,reverse=False)
         
print(desd)
print(aesd)