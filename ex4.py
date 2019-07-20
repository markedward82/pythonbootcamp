cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers /cars_driven


#print out string and variable value of cars
print ("There are", cars, "carsavailable.")
#print out string and variable value of drivers
print ("There are only", drivers, "drivers available.")
#print out string and variable value of cars_not_driven
print ("There will be", cars_not_driven, "empty cars today.")
#print out string and variable value of carpool people
print ("We can transport", carpool_capacity, "people today.")
#print out string and variable value of passengers
print ("we have", passengers, "to carpool today.")
#print out string and
print ("We need to put about", average_passengers_per_car, "in each car.")
