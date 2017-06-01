#set total number of cars
cars = 100
#set spaces per car
space_in_a_car = 4
#set number of drivers and passengers
drivers = 30
passengers = 90
#calculate how many cars won't have drivers
cars_not_driven = cars-drivers
#set cars driven equal to number of drivers
cars_driven = drivers
#calculate total passenger carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#calculate average number of passengers
average_passengers_per_car = passengers/cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
