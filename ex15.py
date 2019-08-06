#ex15  reading file

from sys import argv

#set script and filename to argv
script, filename = argv

#calling open to reach file
txt = open(filename)

#display file name with formatted 
print(f"Here's your file {filename}:")

#use txt to call a function to read.
print(txt.read())

#a string requests to display input
print("I'll also ask you to type it agian:")
#create a variable takes file name user want to open
file_again = input("=>")

#use open function to read the file name from input and save the 
#reading outcome to a variable
txt_again = open(file_again)

#print the data it reads from the input file name.
print(txt_again.read())







