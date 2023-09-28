import random

#gather all the characters to form the password
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!@#$^%&*()_+-=[]{};:<>/,'
numbers = "0123456789"
all = lower + upper + symbols + numbers

#Determine the password length
passwordLength = int(input("Set your password length: "))
print("\n")

password = ''
#Generate a new password based on user input
for i in range (passwordLength):
    password = ''.join([password,random.choice(all)])

print ("Your generated password is:",password)
    