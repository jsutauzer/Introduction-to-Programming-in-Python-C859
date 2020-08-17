#COMP 1 EDITS - CORRECTIONS
# Create a string value and determine if the string consists of only lowercase characters. Print the results.
# expected outcome: True or False
mystring = 'this is a String'
print(mystring.islower())
# THIS SOLUTION DOES NOT GIVE AN OUTPUT

# Use the given username and phone to create a message that lets the user know that you will be calling
# at a specified number for your appointment. Use the format method to insert data into the printed message.
# expected outcome: Hi, Allen. I will call you at 888-555-0011 for our appointment.
username = 'Allen'
phone = 8885550011
phone2= str(phone)
print('Hi, ' + username + '. I will call you at ' + phone2[:3]+'-'+phone2[3:6]+'-'+phone2[6:] + ' for our appointment.')


# THIS SOLUTION WORKS, HOWEVER, THERE MAY BE AN EASIER OPTION.  CONSIDER USING SLICING TO SEPARATE THE PHONE NUMBER INTO SECTIONS.

#COMP 2 EDITS - CORRECTIONS
# starting with year 2000, create a list containing 5 leap years
# when the list is complete, print the full list with a message
# expected outcome: These are the leap years: [2000, 2004, 2008, 2012, 2016]
years = list(range(2000, 2019))
leapYears = []
count = 0
for year in years:
    if year % 4 == 0:
        leapYears.insert(count, year)
        count += 1
print(leapYears)

# THE SOLUTION ABOVE WORKS, BUT CONSIDER HOW YOU WOULD SOLVE THIS TASK WITH A FOR LOOP

# create a tuple to store the WGU phone number 877-435-7948. Store the phone number as three groups of numbers without the hyphens.
phone = ("877", "435", "7948")
print(phone)


# use the tuple to print the last four digits of the phone number
# expected outcome: 7948
print(phone[2])

# THE SOLUTION ABOVE WORKS, BUT CONSIDER USING THE INDEX NUMBER OF THE LAST FOUR DIGITS OF THE PHONE NUMBER

# use the tuple to print the entire phone number with the message to Call WGU now
# expected outcome: Call WGU now at 877-435-7948
print("Call WGU now at " + phone[0] + '-' + phone[1] + '-' + phone[2])

# THE SOLUTION ABOVE WORKS, BUT CONSIDER USING THE INDEX NUMBER OF THE LAST FOUR DIGITS OF THE PHONE NUMBER

#Finish the fruitFunction2 to take as input a list of fruits and return a string value letting us know if the avocado is in the list or not. If so, state that the avocado is in the list. If not, state avocado not found.
def fruitFunction2(fruits):
    if 'avocado' in fruits:
        return 'avocado is in the list'
    else:
        return 'avocado not found'
print(fruitFunction2(['banana','apple','orange','grapes','pineapple']))  #expected outcome: avocado not found
print(fruitFunction2(['mango','avocado','pear']))    #expected outcome: avocado is in the list

# YOU ARE NOT GETTING THE EXPECTED OUTCOME FOR THE TWO CALLS TO FRUITFUNCTION2 ABOVE.

#Complete costCount that takes one argument as a list of expenses and returns the total cost of all purchases
def costCount(purchases):
    total = sum(purchases)
    return total
print(costCount([39.90, 40.21, 8.73, 9.57]))    #expected output: 98.41
print(costCount([139.90, 10.11, 1.53, 3.57]))    #expected output: 155.10999999999999

# DO YOU KNOW WHERE "None" CAME FROM?  DO THE INSTRUCTIONS ASK THAT YOU PRINT THE RESULTS OR RETURN THE RESULTS?


#COMP 3 EDITS - CORRECTIONS
## ---- Random Module --- ##
import random

# use the random module to print a random integer between 2 and 20, exclusive
print(random.randint(2, 19))

# THE SOLUTION ABOVE WOULD ALLOW 20 TO BE INCLUDED AS A POSSIBLE OUTPUT.  HOW WOULD YOU EXCLUDE IT?