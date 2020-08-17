# declare 3 variables with one assignment statement and assign each one an integer value
a, b, c = 1, 2, 3



# convert each of your previous variables to float objects

a = float(a)
b = float(b)
c = float(c)


# convert each of your previous variables to string objects

a = str(a)
b = str(b)
c = str(c)




# Print the result of dividing 783.56 by 123.2 and ensure that the answer results in an integer
# expected outcome: 6

div = int(783.56 / 123.2)
print(div)



# Determine if 2019 is a leap year and print the result.
# expected outcome: 3

leapyear = 2019 % 4
print(leapyear)



# print the calculated length of myFirstString.
# expected outcome: 35

myFirstString = 'I love working with Python so much!'
print(len(myFirstString))



# Create a string value and print it with the first letter of each word capitalized using a Python method.

mystring = 'this is my test string.'
print(mystring.title())




# Create a string value and determine if the string consists of only lowercase characters. Print the results.
# expected outcome: True or False
mystring = 'this is a String'
mystring.islower()


# Use the given variable to construct a python statement that counts how many times the word pizza is used. Print the final count.
# expected outcome: 3
commercial = 'In the Little Ceasars pizza commercial the character says, "pizza, pizza"!'
print(commercial.count('pizza'))




# Use the given username and phone to create a message that lets the user know that you will be calling
# at a specified number for your appointment. Use the format method to insert data into the printed message.
# expected outcome: Hi, Allen. I will call you at 888-555-0011 for our appointment.
username = 'Allen'
phone = 8885550011
parsedPhone = format(int(str(phone)[:-1]), ",").replace(",", "-") + str(phone)[-1] # solution from Stack Overflow https://stackoverflow.com/questions/7058120/whats-the-best-way-to-format-a-phone-number-in-python
message = 'Hi, {}. I will call you at {} for our appointment.'.format(username, parsedPhone)
print(message)
