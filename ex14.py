#ex14: prompting and Passing

#input and argv together

#calling module sys and import package argv
from sys import argv

#set argv variables
script, user_name = argv
#set a string to a variable
prompt = '> '

#made some mistakes on parenthesis
print(f"Hi, {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions?")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"where do you live, {user_name}")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking me.
You live in {lives}. Not sure where it is.
And you have {computer}. Nice.""")


