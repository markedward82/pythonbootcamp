#ex20

#functions and files

from sys import argv

#assign arguements to argv
script, input_file = argv

#create a function will read the file
def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

#display a string
print("First let's print the whole file:\n")
#calling function
print_all(current_file)

#display rewind string
print("now let's rewind, kind of like a tape.")
rewind(current_file)

#display each line string
print("Let's print 3 lines.")

#assign a variable to 1
current_line = 1

#calling function of print_a_line
print_a_line(current_line, current_file)

#increment the line to 2
current_line += 1
print_a_line(current_line, current_file)

#increment the line to 3
current_line += 1
print_a_line(current_line, current_file)

    
