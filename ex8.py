#ex8 printing, printing

#setting string formatted variables in one variable
formatter = "%r %r %r %r"

#the following display the formatted variable with assign data types
print(formatter %(1, 2, 3, 4))
#made a little mistake on the last parenthesis
print(formatter %("one", "two", "three", "four"))
print(formatter %(True, False, False, True))
print(formatter %(formatter, formatter, formatter, formatter))
#the third string has a different quotation
print(formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")
    )
    



