user_name=input("Enter your name: ")
if user_name.isalpha():
    print(f"The name is: {user_name}")
    email=input("Enter your e-mail: ")
    if "@" in range(len(email)-1) and "." in email and email[-1] != "." and email.index(".") > email.index("@"):
      print(f"The e-mail is:{email} ")
    else:
       print("The e-mail is wrong ")
else:
   print("Invalid name, enter the name right")
   