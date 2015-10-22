# -*- coding:utf-8 -*-
# There are 100 cars
cars = 100
# Every car can hold 4 passengers.
space_in_a_car = 4.0
# There are 30 drivers.
drivers = 30
# There are 90 passengers in total.
passengers = 90
# Calculate the number of not-driven cars.
cars_not_driven = cars - drivers
# Calculate the number of cars driven today.
cars_driven = drivers
# Total passengers to be transport in today.
carpool_capacity = cars_driven * space_in_a_car
# How many passengers per car when transporting.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaliable."
print "There are only", drivers, "drivers avaliable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills
# car_pool_capacity is a variable not defined. in this case, we can't use it directly. Varibales in Python doesn't need the statement before use it, but it is necessary to define it.
# 1. In this case, nothing happens when using just 4 not 4.0
# 2. done
# 3.