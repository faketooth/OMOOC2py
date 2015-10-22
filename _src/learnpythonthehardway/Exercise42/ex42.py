# -*- coding: utf-8 -*-
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## is-a 
class Dog(Animal):
	def __init__(self, name):
		## ??
		self.name = name
		
## is-a
class Cat(Animal):
	def __init__(self, name):
		## ??
		self.name = name
		
## is-a
class Person(object):
	def __init__(self, name):
		## ??
		self.name = name
		## Person has-a pet of some kind
		self.pet = None
		
## is-a
class Employee(Person):
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary
		
## is-a
class Fish(object):
	pass
	
## is-a
class Salmon(Fish):
	pass
	
## is-a
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## mary has-a satan which is a cat
mary.pet = satan

## frank is-a employee 
frank = Employee("Frank", 120000)

## frank has-a pet, which is a rover
frank.pet = rover

## flipper is-a fish 
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()