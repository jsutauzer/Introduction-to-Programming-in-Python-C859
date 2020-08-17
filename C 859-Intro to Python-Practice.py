#!/usr/bin/env python
# coding: utf-8

# # Chapter 8: Practice
Task 1

Complete the function to print the first X number of characters in the given string

# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
# Student code goes here
 
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)
# In[1]:


def printFirst(mystring, x):
# Student code goes here
    print(mystring[:x])
# expected output: WGU
printFirst('WGU College of IT', 3)    
 
# expected output: WGU College
printFirst('WGU College of IT', 11)

Task 2

Complete the function to return the last X number of characters in the given string

# Complete the function to return the last X number of characters
# in the given string
def getLast(mystring, x):
# Student code goes here
 
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))


# In[2]:


def getLast(mystring, x):
# Student code goes here
    return mystring[-x:]
# expected output: IT
print(getLast('WGU College of IT', 2))
 
# expected output: College of IT
print(getLast('WGU College of IT', 13))

Task 3

Complete the function to return True if the word WGU exists in the given string otherwise return False

# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
# Student code goes here
    
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
print(containsWGU('Night Owls Rock'))


# In[3]:


def containsWGU(mystring):
# Student code goes here
    if 'WGU' in mystring:
        return True
    else:
        return False
# expected output: True
print(containsWGU('WGU College of IT'))
    
# expected output: False
print(containsWGU('Night Owls Rock'))

Task 4

Complete the function to print all of the words in the given string

# Complete the function to print all of the words in the given string
def printWords(mystring):
# Student code goes here
    
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')


# In[4]:


def printWords(mystring):
# Student code goes here
    print(mystring.split())
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')

Task 5

Complete the function to combine the words into a sentence and return a string

# Complete the function to combine the words into a sentence and return a string 
def combineWords(words):
# Student code goes here
    
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))


# In[5]:


def combineWords(words):
# Student code goes here
    return ' '.join(words)
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))

Task 6

Complete the function to replace the word WGU with Western Governors University and print the new string

# Complete the function to replace the word WGU with Western Governors University
# and print the new string
def replaceWGU(mystring):
# Student code goes here
    
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')


# In[6]:


def replaceWGU(mystring):
# Student code goes here
    print(mystring.replace('WGU', 'Western Governors University'))
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')

Task 7

Complete the function to remove the word WGU from the given string ONLY if it's not the first word and return the new string

# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
# Student code goes here
    
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))


# In[7]:


def removeWGU(mystring):
# Student code goes here
    if 'WGU' == mystring[:3]:
        return mystring
    else:
        return mystring.replace('WGU', '')
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
    
# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))

Task 8

Complete the function to remove trailing spaces from the first string and leading spaces from the second string and return the combined strings

# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
# Student code goes here
    
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))


# In[8]:


def removeSpaces(string1, string2):
# Student code goes here
    return string1.strip() + string2.strip()
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))

Task 9

Complete the function to print the specified hourly rate with two decimals

# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
# Student code goes here
 
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# expected output: $24.12
displayHourlyRate(24.123456)


# In[9]:


def displayHourlyRate(rate):
# Student code goes here
    print("$%.2f" % rate)
# expected output: $34.79
displayHourlyRate(34.789123)    
 
# expected output: $24.12
displayHourlyRate(24.123456)

Task 10

Complete the function to return the number of uppercase letters in the given string

# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
# Student code goes here

# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))


# In[10]:


def countUpper(mystring):
# Student code goes here
    count = 0
    for i in mystring:
        if i.isupper():
            count+=1
    return  count
# expected output: 4
print(countUpper('Welcome to WGU'))
 
# expected output: 2
print(countUpper('Hello, Mary'))


# # Chapter 9: Practice
Task 1

Complete the function to return the first two items in the given list

# Complete the function to return the first two items in the given list
def getFirstTwo(mylist):
# Student code goes here
 
# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))  
 
# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))


# In[11]:


def getFirstTwo(mylist):
# Student code goes here
    return mylist[:2]
# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))  
 
# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))

Task 2

Complete the function to return the last two items in the given list

# Complete the function to return the last two items in the given list
def getLastTwo(mylist):
# Student code goes here
 
# expected output: [2, 10]
print(getLastTwo([8,3,5,2,10]))  
 
# expected output: [9, 12]
print(getLastTwo([15,2,9,12]))


# In[12]:


def getLastTwo(mylist):
# Student code goes here
    return mylist[-2:]
# expected output: [2, 10]
print(getLastTwo([8,3,5,2,10]))  
 
# expected output: [9, 12]
print(getLastTwo([15,2,9,12]))

Task 3

Complete the function to add num1 to the end of the given list

# Complete the function to add num1 to the end of the given list
def addToEnd(mylist, num1):
# Student code goes here
 
# expected output: [4, 5, 6, 7]
print(addToEnd([4,5,6], 7))
 
# expected output: [9, 8, 7, 6]
print(addToEnd([9,8,7], 6))


# In[13]:


def addToEnd(mylist, num1):
# Student code goes here
    mylist.append(num1)
    return mylist
# expected output: [4, 5, 6, 7]
print(addToEnd([4,5,6], 7))
 
# expected output: [9, 8, 7, 6]
print(addToEnd([9,8,7], 6))

Task 4

Complete the function to add num2 to the front of the given list

# Complete the function to add num2 to the front of the given list
def addToFront(mylist, num1):
# Student code goes here
 
# expected output: [3, 4, 5, 6]
print(addToFront([4,5,6], 3))
 
# expected output: [10, 9, 8, 7]
print(addToFront([9,8,7], 10))


# In[14]:


def addToFront(mylist, num1):
# Student code goes here
    mylist.insert(0, num1)
    return mylist
# expected output: [3, 4, 5, 6]
print(addToFront([4,5,6], 3))
 
# expected output: [10, 9, 8, 7]
print(addToFront([9,8,7], 10))

Task 5

Complete the function to return a new list containing the first two and last two items in the given list

# Complete the function to return a new list containing 
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
# Student code goes here
 
# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
 
# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))


# In[15]:


def getFirstTwoAndLastTwo(mylist):
# Student code goes here
    newlist = mylist[:2] + mylist[-2:]
    return newlist
# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))
 
# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))

Task 6

Complete the function to remove the first item in the given list

# Complete the function to remove the first item in the given list
def removeFirst(mylist):
# Student code goes here
 
# expected output: [7, 8, 9]
print(removeFirst([6,7,8,9]))
 
# expected output: [2, 3, 4]
print(removeFirst([1,2,3,4]))


# In[16]:


def removeFirst(mylist):
# Student code goes here
    mylist.pop(0)
    return mylist
# expected output: [7, 8, 9]
print(removeFirst([6,7,8,9]))
 
# expected output: [2, 3, 4]
print(removeFirst([1,2,3,4]))

Task 7

Complete the function to remove the third item in the given list

# Complete the function to remove the third item in the given list
def removeThird(mylist):
# Student code goes here
 
# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))
 
# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))

# In[17]:


def removeThird(mylist):
# Student code goes here
    mylist.pop(2)
    return mylist
# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))
 
# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))

Task 8

Complete the function to order the values in the list. If ascending is true then order lowest to highest otherwise sort highest to lowest

# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
# Student code goes here
 
# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))
 
# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))

# In[18]:


def sortList(mylist, ascending):
# Student code goes here
    mylist.sort(reverse = ascending)
    return mylist
# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))
 
# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))

Task 9

Complete the function to return a dictionary using list1 as the keys and list2 as the values

# Complete the function to return a dictionary using 
# list1 as the keys and list2 as the values
def createDict(list1, list2):
# Student code goes here
        
# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}  
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))        
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))

# In[19]:


def createDict(list1, list2):
# Student code goes here
    mydict = dict(zip(list1,list2))
    return mydict
# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}  
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))        
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))

Task 10

Complete the function to return a dictionary value if it exists or return Not Found if it doesn't exist

# Complete the function to return a dictionary value 
# if it exists or return Not Found if it doesn't exist
def findDictItem(mydict, key):
# Student code goes here
        
# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))

# In[20]:


def findDictItem(mydict, key):
# Student code goes here
    if key in mydict:
        return mydict.get(key)
    else:
        return 'Not Found'
# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))

Task 11

Complete the function to remove a dictionary item if it exists

# Complete the function to remove a dictionary item if it exists
def removeDictItem(mydict, key):
# Student code goes here
 
# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))

# In[21]:


def removeDictItem(mydict, key):
# Student code goes here
    if key in mydict.keys():
        mydict1 = mydict.pop(key)
        return mydict
    else:
        return mydict
# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))
 
# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'},'Cameroon'))

Task 12

Complete the function to print every key and value

# Complete the function to print every key and value
def printDict(mydict):
# Student code goes here
        
# expected output: 
#        tomato=red
#        banana=yellow
#        lime=green
printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})
 
# expected output: 
#        Brazil=Brasilia
#        Ireland=Dublin
#        Indonesia=Jakarta
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})

# In[ ]:





# # Chapter 11: Practice

Task 1

Complete the function that takes an integer as input and returns the factorial of that integer

from math import factorial

def calculate(x):
# Student code goes here
 
print(calculate(3)) #expected outcome: 6
print(calculate(9)) #expected outcome: 362880

# In[22]:


from math import factorial

def calculate(x):
# Student code goes here
    return factorial(x)
 
print(calculate(3)) #expected outcome: 6
print(calculate(9)) #expected outcome: 362880

Task 2

Complete the function that takes a list as input and returns a randomized item from that list

import random as r

def selection(x):
# Student code goes here
 
print(selection(['apple','banana','orange','grape']))
print(selection([7,5,3,9,12,4,8,10]))

# In[23]:


import random as r

def selection(x):
# Student code goes here
    return r.choice(x)
 
print(selection(['apple','banana','orange','grape']))
print(selection([7,5,3,9,12,4,8,10]))

Task 3

Complete the function that takes as input an integer for a number of days and prints the total number of seconds in that number of days

import datetime

def currentDate(x):
# Student code goes here
 
currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.

# In[24]:


import datetime

def currentDate(x):
# Student code goes here
    
    print(datetime.timedelta(days=x).total_seconds())
 
currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.

Task 4

Complete the function to return the current date

import datetime as dt

def currentDate():
# Student code goes here
 
print(currentDate()) #Expected outcome will vary, but should follow this format: The current date is 9-11-2018.

# In[25]:


import datetime as dt

def currentDate():
# Student code goes here
    date = dt.date.today()
    return 'The current date is ' + f"{date:%m-%d-%y}"
 
print(currentDate()) #Expected outcome will vary, but should follow this format: The current date is 9-11-2018.

Task 5

Complete the function that takes an integer as input, multiplies by e, and returns result rounded up

from math import e,ceil

def mathCalculation(x):
# Student code goes here
 
#expected outcome: 9
print(mathCalculation(3))    

#expected outcome: 25
print(mathCalculation(9))

# In[26]:


from math import e,ceil

def mathCalculation(x):
# Student code goes here
    num = e*x
    return ceil(num)

#expected outcome: 9
print(mathCalculation(3))    

#expected outcome: 25
print(mathCalculation(9))

Task 6

Complete the function to return the number of leap years in the list

import calendar

# Complete the function to return the number of leap years in the list
def countLeapYears(yearList):
# Student code goes here
 
# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))
 
# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))

# In[27]:


import calendar

# Complete the function to return the number of leap years in the list
def countLeapYears(yearList):
# Student code goes here
    count = 0
    for i in yearList:
        if calendar.isleap(int(i)):
            count += 1
    return  count
    
# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))
 
# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))

Task 7

Complete the function to print the full name of the month using the calendar library

import calendar

# Complete the function to print the full name of the month using the calendar library 
def printMonthName(monthNum):
# Student code goes here
 
# expected output: March
printMonthName(3)
 
# expected output: November
printMonthName(11)

# In[28]:


import calendar

# Complete the function to print the full name of the month using the calendar library 
def printMonthName(monthNum):
# Student code goes here
    name = calendar.month_name[monthNum]
    print(name)
# expected output: March
printMonthName(3)
 
# expected output: November
printMonthName(11)

Task 8

Complete the function to print the full name of the day of the week

import calendar, datetime

# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
# Student code goes here
 
# expected output: Friday    
printWeekdayName(2001, 8, 31)
 
# expected output: Monday
printWeekdayName(2018, 10, 1)

# In[29]:


import calendar, datetime

# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
# Student code goes here
    dayofweek = datetime.date(year, month, day).strftime("%A")
    print(dayofweek)
    
# expected output: Friday    
printWeekdayName(2001, 8, 31)
 
# expected output: Monday
printWeekdayName(2018, 10, 1)

Task 9

Complete the following function to return a random number between 5 and 8 exclusive

import random

# Complete the following function to return a random number
# between 5 and 8 exclusive
def getRandom():
# Student code goes here
 
# expected output: You should only get 5s, 6s, and 7s
for i in range(10):
    print(getRandom())
    
# In[30]:


import random

# Complete the following function to return a random number
# between 5 and 8 exclusive
def getRandom():
# Student code goes here
    num = random.randrange(5,8)
    return num
    
# expected output: You should only get 5s, 6s, and 7s
for i in range(10):
    print(getRandom())

Task 10

Complete the function to add 90 days to the given date and return the new date

import datetime

# Complete the function to add 90 days to the given date and return the new date
def add90Days(someDate):
# Student code goes here
 
# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))
 
# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))

# In[31]:


import datetime

# Complete the function to add 90 days to the given date and return the new date
def add90Days(someDate):
# Student code goes here
    date = someDate + datetime.timedelta(days = 90)
    return date
# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))
 
# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))


# # Chapter 12: Practice

Task 1

Complete the function to return the directory name only from the given file name

import os

# Complete the function to return the current working directory
def getCurrentDirectory():
# Student code goes here
 
# expected output: /tmp
# if using PyFiddle.io otherwise it varies
print(getCurrentDirectory())

# In[32]:


import os

# Complete the function to return the current working directory
def getCurrentDirectory():
# Student code goes here
    return os.getcwd()

# expected output: /tmp
# if using PyFiddle.io otherwise it varies
print(getCurrentDirectory())

Task 2

Complete the function to return the directory name only from the given file name

import os

# Complete the function to return the directory name only from the given file name
def getDirectoryName(fileName):
# Student code goes here
 
# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))
 
# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))

# In[33]:


import os

# Complete the function to return the directory name only from the given file name
def getDirectoryName(fileName):
# Student code goes here
    return os.path.basename(fileName)
    
# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))
 
# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))

Task 3

Complete the function to return the file name part only from the given file name

import os

# Complete the function to return the file name part only from the given file name
def getFileName(fileName):
# Student code goes here
 
# expected output: test.html
print(getFileName("/var/www/test.html"))
 
# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))

# In[34]:


import os

# Complete the function to return the file name part only from the given file name
def getFileName(fileName):
# Student code goes here
    return os.path.dirname(fileName)
    
# expected output: test.html
print(getFileName("/var/www/test.html"))
 
# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))

Task 4

Complete the function to return the directory name only from the given file name

import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
# Student code goes here
 
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))

# In[35]:


import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
# Student code goes here
    return open(filename, "w")
    
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))

Task 5

Complete the function to print all files in the given directory

import os

# Complete the function to print all files in the given directory
def printFiles(someDirectory):
# Student code goes here
    
# expected output: main.py    
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())

# In[36]:


import os

# Complete the function to print all files in the given directory
def printFiles(someDirectory):
# Student code goes here
    print(os.listdir(someDirectory))
    
# expected output: main.py    
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())

Task 6

Complete the function to return FILE if the given path is a file or return DIRECTORY if the given path is a directory or return NEITHER is it's not a file or directory

import os

# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
def whatIsIt(somePath):
# Student code goes here

# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))
 
# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))
 
# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))

# In[37]:


import os

# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
def whatIsIt(somePath):
# Student code goes here
    if os.path.isfile(somePath):
        return 'FILE'
    elif os.path.isdir(somePath):
        return 'Directory'
    else:
        return 'Neither'

# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))
 
# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))
 
# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))

Task 7

Complete the function to read the contents of the specified file and print the contents

import os

# Complete the function to read the contents of the specified file and print the contents
def printFileContents(filename):
# Student code goes here
 
# expected output: Hello
with open("test.txt", 'w') as f: 
f.write("Hello")
printFileContents("test.txt")

# In[38]:


import os

# Complete the function to read the contents of the specified file and print the contents
def printFileContents(filename):
# Student code goes here
    with open(filename, "r") as f:
        contents = f.read()
        return contents
    
# expected output: Hello
with open("test.txt", 'w') as f: 
    f.write("Hello")
printFileContents("test.txt")

Task 8

Complete the function to append the given new data to the specified file then print the contents of the file

import os

# Complete the function to append the given new data to the specified file then print the contents of the file
def appendAndPrint(filename, newData):
# Student code goes here
 
# expected output: Hello World
with open("test.txt", 'w') as f: 
f.write("Hello ")
appendAndPrint("test.txt", "World")

# In[39]:


import os

# Complete the function to append the given new data to the specified file then print the contents of the file
def appendAndPrint(filename, newData):
# Student code goes here
    with open(filename, "a+")as f:
        appended = f.write(newData)
    with open(filename, "r")as r:
        contents = r.read()
        return contents
    
# expected output: Hello World
with open("test.txt", 'w') as f: 
    f.write("Hello ")
appendAndPrint("test.txt", "World")


# In[ ]:




