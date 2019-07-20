my_name = 'Mark Yo'
my_age = 37 #not a lie
my_height = 171*0.393700787 #inches
my_weight = 250 #lbs
my_eyes = 'Black'
my_teeth = 'Yellow'
my_hair = 'Black'

#A String with % which print out the string value
print("Let's talk about %s." % my_name)
#a text with % leads out the double variable
print("He's %d inches tall." % my_height)
#this text comes with %d that leads double variable
print("He's %d pounds heavy." % my_weight)
#A string contains single quote may cause syntax problem
print("Actually that's not too heavy.")
#A string with 2s % that lead 2 string variables
print("he's got %s eyes and %s hair." % (my_eyes, my_hair))
#A string with %s that leads a string varialbe
print("His teeth are usually %s depending on the coffee." % my_teeth)

#using %d to do calculation in the string
print ("If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age+my_height+my_weight))


