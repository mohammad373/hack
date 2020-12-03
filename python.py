# hack
import os
from colorama import Fore
print("hello welcome back ;)")
a = int(input("Enter Your Number One ==>  "))
b =  int(input("Enter Your Number Two ==>  "))
x = a ** b
print("your number is {x}")
c = int(input("Enter Your Number For Turn Off ==>  "))
os.system(f"shutdown /s /t {c}")



