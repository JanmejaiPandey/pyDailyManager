from align import Align
from mongoConnect import tasksDB
import os
import time

Align.centerAlign("Welcome to the Manager")

print("\n")

Align.centerAlign("Tasks Remaining")

print("\n")

time.sleep(1)

tasksDB.showTask()

print("want to add new task?(y/n)")

ans = input()

while(ans == 'y'):
    print("Enter new task")
    newtask = input()
    tasksDB.addTask(newtask)
    print("\nwant to add more new task?(y/n)")
    ans = input()

print("press any key to exit!")
input()
os.system('exit')
