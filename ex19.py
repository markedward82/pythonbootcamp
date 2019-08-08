#ex19 functions and variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party")
    print("get a blanket.\n")
    
#display a string  
print("We can just give function numbers directly:")
#calling a function and give 20, 30 as arguements
cheese_and_crackers(20, 30)

#display a string
print("OR, we can use variables from our script.")
#assign numbers to variables
amount_of_cheese = 10
amount_of_crackers = 50

#assign variables to function arguement
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#display a string
print("We can even do math inside, too")
#giving operation in the arguement
cheese_and_crackers(10+20, 5+6)

#display a string
print("And we can combine the two, variables and math")
#variables and operation together.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

