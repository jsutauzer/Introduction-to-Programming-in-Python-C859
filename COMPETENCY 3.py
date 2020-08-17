# ---- Math Module --- ##
import math

# use the math module to determine the factorial of the number 7 and print the result
# expected outcome: 5040
print(math.factorial(7))

# use the math module to determine the square root of the number 27 and print the result
# expected outcome: 5.196152422706632
print(math.sqrt(27))

# use the math module to determine the largest integer less than or equal to 15.87 and print the result
# expected outcome: 15
print(math.floor(15.87))

# use the math module to determine the smallest integer integer greater than or equal to 15.87 and print the result
# expected outcome: 16
print(math.ceil(15.87))

# use the math module to determine e to the power of 4
# expected outcome: 54.598150033144236
print(math.exp(4))


## ---- Random Module --- ##
import random

# use the random module to print a random integer between 2 and 20, exclusive
print(random.randint(2, 20))

# use the random module to print a random number from the range 1 to 100, inclusive
print(random.randrange(1, 101))

# use the random module to return a random floating point number
print(random.random())

# Create a list of 6 words. Then use the random module to return a random element from that list.
mylist = ('name1', 'mike', 'jelly', 'word4', 'six')
print(random.choice(mylist))

## ---- OS Module --- ##
import os

# use the os module to create a hard link to C://myfile.txt at C://myPython/myfile.txt
my_link = os.link(src= "myfile.txt", dst = "C:\\myPython\\myfile.txt")

# use the os module to delete the file C://myfile.txt
os.remove("C:\\myfile.txt")


# use the os module to return the current working directory
print(os.getcwd())

# use the os module to change the root directory to C://home/
os.chroot('C:\\home')

## ---- Datetime Module --- ##
import datetime

# use the datetime module to print the current year
dt = datetime.datetime.now()
print(dt.year)

# use the datetime module to print the current month
dt = datetime.datetime.now()
print(dt.month)


# use the datetime module to print the current day
dt = datetime.datetime.now()
print(dt.day)


# use the datetime module to print the total number of seconds in 4 days
# expected outcome: 345600.0
four_days = datetime.timedelta(days=4)
print(four_days.total_seconds())

# print today's date one year from now
dt = datetime.datetime.now()
print(dt + datetime.timedelta(days=365))

## ---- Lookup  --- ##
# You need to use the datetime library to account for time zone adjustments, but aren't sure which method(s) to use.
# You are taking an exam and can't google it. What Python function will allow you to look up and locate the method?
# Write your code below:
help(datetime)
