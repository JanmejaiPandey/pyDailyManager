from align import Align
from mongoConnect import usersDB
import os,time

Align.centerAlign("Register To the Manager")

print("Enter Email ID:")
email = input()

print("Enter Password:")
password = input()

usersDB.addUser(email,password)

time.sleep(2)
os.system("cls")
os.system("python login.py")