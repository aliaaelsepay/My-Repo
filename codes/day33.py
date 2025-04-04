"""
def show(x):
    print("iti")
    return(x)
y=show("hello")
print(y)  #### execute the function first and then return the value in call 

def addnum(x,y):
    return(x+y)
result=addnum(2,3)
print(result)



def area(x,y,z=1):
    return x*y*z
print(area(2,3,6))
print(area(2,3))

def area(*x) #### collaction of values
   z=0
   for i in x:
     z+=1
     return(z)
   print(area(1,2,3,4,5)) 
"""
users=[{"name":"omar","pass":123},{"name":"ahmed","pass":456}]
user_name=input("Enter you name: ")
for i in range(len(users)):
    if user_name in users[i]:
        print("The name is right")
    else:
        print("The name is wrong")