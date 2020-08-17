# Create a string value and determine if the string consists of only lowercase characters. Print the results.
# expected outcome: True or False
mystring = 'this is a String'
mystring.islower()
# THIS SOLUTION DOES NOT GIVE AN OUTPUT


# Use the given username and phone to create a message that lets the user know that you will be calling
# at a specified number for your appointment. Use the format method to insert data into the printed message.
# expected outcome: Hi, Allen. I will call you at 888-555-0011 for our appointment.
username = 'Allen'
phone = 8885550011
parsedPhone = format(int(str(phone)[:-1]), ",").replace(",", "-") + str(phone)[-1] # solution from Stack Overflow https://stackoverflow.com/questions/7058120/whats-the-best-way-to-format-a-phone-number-in-python
message = 'Hi, {}. I will call you at {} for our appointment.'.format(username, parsedPhone)
print(message)
# THIS SOLUTION WORKS, HOWEVER, THERE MAY BE AN EASIER OPTION.  CONSIDER USING SLICING TO SEPARATE THE PHONE NUMBER INTO SECTIONS.