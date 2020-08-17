# starting with year 2000, create a list containing 5 leap years
# when the list is complete, print the full list with a message
# expected outcome: These are the leap years: [2000, 2004, 2008, 2012, 2016]
leap_years = []
i = 2000
while len(leap_years) < 5:
    leap_years.append(i)
    i += 4
print(leap_years)

# THE SOLUTION ABOVE WORKS, BUT CONSIDER HOW YOU WOULD SOLVE THIS TASK WITH A FOR LOOP

# create a tuple to store the WGU phone number 877-435-7948. Store the phone number as three groups of numbers without the hyphens.
phone = ("877", "435", "7948")
print(phone)


# use the tuple to print the last four digits of the phone number
# expected outcome: 7948
print(str().join(phone[-1:]))

# THE SOLUTION ABOVE WORKS, BUT CONSIDER USING THE INDEX NUMBER OF THE LAST FOUR DIGITS OF THE PHONE NUMBER

# use the tuple to print the entire phone number with the message to Call WGU now
# expected outcome: Call WGU now at 877-435-7948
print("Call WGU now at " + str('-').join(phone))

# THE SOLUTION ABOVE WORKS, BUT CONSIDER USING THE INDEX NUMBER OF THE LAST FOUR DIGITS OF THE PHONE NUMBER

#Finish the fruitFunction2 to take as input a list of fruits and return a string value letting us know if the avocado is in the list or not. If so, state that the avocado is in the list. If not, state avocado not found.
def fruitFunction2(fruits):
    if 'avocado' in fruits:
        return 'avocado not found'
    else:
        return 'avocado is in the list'
print(fruitFunction2(['banana','apple','orange','grapes','pineapple']))  #expected outcome: avocado not found
print(fruitFunction2(['mango','avocado','pear']))    #expected outcome: avocado is in the list

# YOU ARE NOT GETTING THE EXPECTED OUTCOME FOR THE TWO CALLS TO FRUITFUNCTION2 ABOVE.

#Complete costCount that takes one argument as a list of expenses and returns the total cost of all purchases
def costCount(purchases):
    total = sum(purchases)
    print(total)
print(costCount([39.90, 40.21, 8.73, 9.57]))    #expected output: 98.41
print(costCount([139.90, 10.11, 1.53, 3.57]))    #expected output: 155.10999999999999

# DO YOU KNOW WHERE "None" CAME FROM?  DO THE INSTRUCTIONS ASK THAT YOU PRINT THE RESULTS OR RETURN THE RESULTS?
