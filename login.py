import mongoConnect
import os,time
from mongoConnect import verify,names
from align import Align

# print(mongoConnect.colNames())
# print(names.colNames())
# print(verify.checkUser(email))

Align.centerAlign("Login To the Manager")

print("Enter Email ID:")
email = input()

print("Enter Password:")
password = input()

if(verify.checkUser(email)):
    if(verify.checkPass(password)):
        time.sleep(1)
        os.system('cls')
        os.system('python main.py')
    else:
        print("Wrong Password")  
else:
    print("User Does'nt Exist!!")
    print("Do you want to register yourself(y/n)")
    ans = input()
    if(ans=='y'):
        os.system('cls')
        os.system('python register.py')
    elif(ans=='n'):
        os.system('exit')

