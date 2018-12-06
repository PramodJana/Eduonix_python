user = input("Enter your username: ")
file_object = open("username.txt","a")
file_object.write(user+"\n")
file_object.close()

file_object2 = open("username.txt","r")

userlist= file_object2.read()
print (userlist)

file_object2.close()
