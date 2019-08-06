# ex16 
# new functions
# Close function
# read function
# readline function
# truncate function
# write function

#import the package
from sys import argv

#set script and filename as arguments. 
script, filename = argv

#display a string with formatted variable
print(f"We're going to erase {filename}")

#display string
print("If you don't want that, hit CTRL-C (^C)")
#display string
print("If you do want that, hit RETURN.")

input("?")

#display string
print("Opening the file...")
#set target variable to collect the file
target = open(filename, 'w')

#display string
print("Truncating the fiel. Goodbye!")
target.truncate()

#display sentences
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#display sentences
print("I'm going to write these to the file.")

#target calling function and write the line1 to target
target.write(line1)
#target calls function (write) with string to change line
target.write("\n")

#target calls function (write) and write line2 to target
target.write(line2)
#target calls function (write) and change the line
target.write("\n")

#target calls function (write) and write line3 to target
target.write(line3)
#target calls function (write) with string to change line
target.write("\n")

#"r" Opens a file for reading only.
#"r+" Opens a file for both reading and writing.
#"rb" Opens a file for reading only in binary format.
#"rb+" Opens a file for both reading and writing in binary format.
#"w" Opens a file for writing only.
#have to change the open condition to read 'r' only it will be able to 
#print the file
print("\n")
print("What did I write:")
target = open(filename,'r')
print(target.read()) 

#print a sentence
print("And finally, we close it.")
#target calls function (close) to stop all other funcitons.
target.close()


