def star():
 number = input("Enter the number: ")
 number=int(number)
 list=[]
 for i in range(1,number+1):
  res=""
  for j in range(1,number+1):
    if(j<=(number-i)):
     res+=" "
    else:
     res+="*"
     list.append(res)  
      #for pyramid in list:
  return(list)
print(star())