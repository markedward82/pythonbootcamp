#ex18 Names, Variables, Code, Function


#Function do three things:
#1. They name pieces of code the way variables name and numbers.
#2. They take arguement the way your script take argv
#3. using #1 and #2 they let you make your own "mini script" or "tiny command"

#you can create a function by using the word def in python
#This one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#Ok, that *args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# this one only take one arguement
def print_one(arg1):
    print(f"arg1:{arg1}")
    
#this one takes no arguement
def print_none():
    print("I got nothing")
    
#execute all the functions
print_two("zed", "shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


