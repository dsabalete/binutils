# -*- coding: utf-8 -*-
# http://learnpythonthehardway.org/book/ex4.html

# Setting value for different variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# Calculate how many cars are not driven
cars_not_driven = cars - drivers

# Calculate how many cars are driven
cars_driven = drivers

# how many people can be moved
carpool_capacity = cars_driven * space_in_a_car

# what is the average number of passengers per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."