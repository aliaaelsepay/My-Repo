def sign():
    users=[{"name":"omar","pass":123},{"name":"ahmed","pass":456}]
    user_name=input("Enter you name: ")
    for i in users:
        if user_name in i["name"]:   #### dic is unorderedddddddddddd
            print(f"The name is right: {user_name}")
            password=input("Enter your password: ")
            password=int(password)

            if password == i["pass"]:
                print("you have access")
                return 
            else:
                print("The password is wrong")
    else:
        print("you have no access")
        
sign()