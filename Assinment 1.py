# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:13:16 2021

@author: admin
"""
#Q1. Print the following statements as a message in python interpreter.

st1= 'Charlie said “We have to buy dinner and I have only $10 with me.”'
print(st1)
st2= "Please get my pencil from Virendra’s bag."
print(st2)

print('Name\tAge \nRita\t10Year\nGeeta\t14Year\nSita\t20Year')

#Q2. Try out these python builtin functions on a string variables : name = “Peter” and password = “$45^123A”.

name= 'Peter'                                            #Output of function:
password='$45^123A'                                       #name           password
print(name.isalnum(),password.isalnum())                  #True           False
print(name.isalpha(),password.isalpha())                  #True           False
#print(name.isascii(),password.isascii())                 #True           True
print(name.isdecimal(),password.isdecimal())              #False          False
print(name.isdigit(),password.isdigit())                  #False          False
print(name.isidentifier(),password.isidentifier())        #True           False
print(name.islower(),password.islower())                  #False          False
print(name.isnumeric(),password.isnumeric())              #False          False
print(name.isprintable(),password.isprintable())          #True           True
print(name.isspace(),password.isspace())                  #False          False
print(name.title(),password.istitle())                    #True           True
print(name.isupper(),password.isupper())                  #False          True

#Q3. Print this whole message in all capital letters and all small letters

st3='Me and My best friend are neighbors. I like o play with my best friend'

print(st3.upper())          #It will print msg in all  capital
print(st3.lower())          #It will print msg in all  lower

#In the statement in Q3., find the occurences of ‘best frined’ and ‘my’. The print the message again by replacing all the occurences of ‘best friend’ with ‘worst enemy’ and ‘like’ with ‘hate’. (Use builtin functions of string data-type when required. )
st3='Me and My best friend are neighbors. I like to play with my best friend '

print(st3.count('best friend'))     #count is 1
print(st3.count('my'))              #count is 1

print(st3.replace('best friend','worst enemy'))
print(st3.replace('like','hate'))

#Q5. Initialise a user provided input string in python and check if it starts with ‘I am’ and ends with ‘school’. Now, swap the case of every letter of the provided string (that is all capital letters would become small letters and vice versa).

st4=input('Enter the string :')
#print(st4)

print(st4.startswith('I am'))
print(st4.endswith('school'))
print(st4.upper())
print(st4.lower())
#Q6. Construct a string of your full-name with all small letters. Then use a string operation to Capitalize all the letters, and print the resulting string. Now use this capitalized string and make only the first letter in each word capital and print the resulting string.
st5='wasim gulab pinjari'
print(st5.upper())
print(st5.title())
#  Q7. Construct a string to represent the statement written below and print it:
print("String is one of python's features")
print('Raj said "I don,t want to go for tthetrip"')
# Q8. Construct a string equivalent to the following sentence:
st6="city name is big city"
print(st6.replace('city name','mumbai'))
print(st6.capitalize())
#Q9. Modify the string "Amar Akbar Anthony" so that when printed, each word will appear on a new line
print("Amar\nAkbar\nAnthony")
#Q10. Consider the string "  Computers are powerful.  ". Notice the spaces before the first and after the last words. Modify the string to remove these, and print the string.
st7="  Computer are powerful  "       
print(st7.strip())
#Q11. For the string in the above example, count the number of times each of the vowels "a", "e", "i", "o", "u" appear in the string.

print(st7.count('a'))
print(st7.count('e'))
print(st7.count('i'))
print(st7.count('o'))
print(st7.count('u'))
