#While you have already been writing strings, you still do not know what they do. in this 
#exercise we create a bunch of variables with complex strings so you can see what they are for. 
#First an explanation of strings.
#A string is usually a bit of text you want to display to someone, or "export" out of the 
#program you are writing. Python knows you want something to be a string when you put either 
#"(double-quotes) or ' (single-quotes) around the text. You saw this many times with your use 
#of print when you put the text you want to go to the string inside " or ' after the print. 
#When you put the text you want to go to the string inside " or ' after the print. Then Python 
#prints it.
#Strings may contain the format characters you have discovered so far. You simply put the 
#formatted variables in the string, and then a % (percent) character, followed by the variable. 
#The only cathc is that if you want mutiple formats in your string to pring multiple variables, 
#you need to put them inside ()(parenthesis) spearated by , (commas). it's as if you were 
#telling to buy you a list of items from the store and you said, "I want mild, eggs, bread, and 
#soup." Only as a programmer we say, "(milk, eggs, bread, soup)".
#We will now type in a whole bunch of strings, variables formats and print them. You will also 
#practice using short abbreviated variable names. Programmers love saving themselves time at 
#your expens by using annoying crptic variable names, so let's get you started being able to 
#read and write them early on.


#Set a string variable with string formatted %10
x = "There are %d types of people." %10
#Set a string variable call binary
binary = "binary"
#set a string variable called don't
do_not = "don't"
#set a string variable with 2 formatted variables
y = "Those who know %s and those who %s." %(binary, do_not)

#display variable x
print(x)
#display vraible y
print(y)

#display a string with formatted variable x
print("I said: %r." %x)
#display a string with a formatted variable y
print("I also said: '%s'." %y)

#set a boolean variable
hilarious = False
#set a string variable with formatted variable inside
joke_evaluation = "Isn't that joke so funny?! %r"

#concate 2 different variables (string and boolean)
print(joke_evaluation % hilarious)

#set a string variable as w
w = "This is the left side of ..."
#set a string variable as e
e = "a string with a right side."

#display 2 string variables with operator +
print(w + e)

p = input("Please type you name: ")
print("Your name is", p)



