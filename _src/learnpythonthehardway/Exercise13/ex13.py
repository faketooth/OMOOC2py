from sys import argv

script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

'''
MacBook-Air:Exercise13 alphonse$ python ex13.py 
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: need more than 1 value to unpack
MacBook-Air:Exercise13 alphonse$ python ex13.py 1 2 3
The script is called: ex13.py
Your first variable is: 1
Your second variable is: 2
Your third variable is: 3
'''