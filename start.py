import os,time
from align import Align

Align.centerAlign("Python Daily Manager")
print("do you want to login(L) or register(R)")
ans = input()
if(ans == 'L'):
    os.system('cls')
    os.system('python login.py')
elif(ans ==  'R'):
    os.system('cls')
    os.system('python register.py')
else:
    print("Wrong Choice Entered")
