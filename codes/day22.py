"""
user_input=input("enter your name: ")
if user_input.isalpha():
print("valid name entered.")
else:
print("invalid input, please use alphabetic characters only.")


num=[1,2,3,4,5]
num.append(4) # add number at last
num.remove(3) # remove element 3
print (num+ [6,7])
print (num*2 )  # repeat list
num.sort()
num.reverse()
x= sorted(num,reverse=True) 

fruits=["apple","banana","cherry"]
fruits1=["mango","peace"]
fruits.extend(fruits1) #  work with lists
fruits.pop() # remove the last element amd take index
print(fruits)

fruits=["apple","banana","cherry"]
del fruits[0] # delete from memory and take indexes
print(fruits)"

fruits=["apple","banana","cherry"]
print("banana" not in fruits) # membership give (true or false) and can use (not in )
text="hello world"
print("world" in text)"

authorized_user=["alisa","bob","charlie"]
user= "alisa"
if user in authorized_user:
    print (f"welcome {user}")
else:
   print ("access denied")

for i in range(5):
    print(i)
    if i==4:
        break # use else with break usually
else:
    print("End")"

user_name = input("Enter your name: ")
while True:
    user_name = input("Enter your name: ")
    if user_name.isalpha():
        print(f"The name is: {user_name}")
        
        email = input("Enter your e-mail: ")
        
        # Check if '@' is in the first 13 characters of the email, 
        # if '.' exists in the email, if it doesn't end with '.', and if '.' comes before '@'.
        if "@" in email[:13] and "." in email and email[-1] != "." and email.index(".") < email.index("@"):
            print(f"The e-mail is: {email}")
            break  # If everything is valid, break out of the loop
        else:
            print("The e-mail is wrong. Please enter a valid email.")
    else:
        print("Invalid name, please enter the name correctly.")
        number=input() # user
number=int(number)
list=[]
for i in range(1,number+1):
 result=""*(number-i)+"*"*i 
 list.append(result)  

for pyramid in list:
   print(pyramid)

number = 4
list=[]
for i in range(1,number+1):
 res=""
 for j in range(1,number+1):
  if(j<=(number-i)):
    res+=" "
  else:
   res+="*"
 list.append(res)  

for pyramid in list:
 print(pyramid)

 while true ### infinty loop
 email.split #### separete email into two parts 


while True:
    name= input("Enter your name: ")
    if name and not name.isdigit():
        break
    else:
        print ("please inter a valid name:")
while True:
    email=input("Enter your email: ")
    if '@' in email and '.' in email:
        username,domain=email.split('@')
        if username and domain:
            x,y= domain.split('.')
            break
        else:
            print("please enter a valid email :")
print(f"\nName: {name}")        
print(f"\nEmail: {name}")

person.get("height","not avaliable")  ## if i dont find height in dic print not avaliable

   

data= {"fruits":["apple","banana","cherry"], "vegetales":["carrot","lecttus","tomato"]
       }
print (data.items())"

person.pop("key")# delete key id dic
person.popitem() # delete last element 
print( list(person.keys())) 
....................................
for key in student :
    print(key,student[key])  ### output values"
.......................................
person1.update(person2) #### update dic"
person.clear( )   ##### remove data and leave the dic empty"
.............................................
def ### before function 
def show():
print ("hello")
show() ##3 we should call the function before print function 
........................................................
def show(x):
    print ("hello")

show()

return in function like break we dont need to do else

"""
