# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:36:30 2021

@author: admin
"""

#Q1. Write a program to add all the natural numbers that are less than 50,divisible by 5 but not divisible by 3.

sum=0
for i in range (1,50):
    if i%5==0 and i%3 !=0:
        sum=sum+i
print('sum of natural number less than 50: ',sum)

#4. Write a program to generate n prime numbers greater than m. The positive integers m, n should be taken from the user.

n=int(input('how many prime number you want to print:'))
m=int(input('print the prime number greter than this:'))
c=0
a=m+1
b=int(a/2)
while True:
    for i in range(2,b):
        if a%i==0:
            break
    else:
        print(a)
        c=c+1
    a+=1
    if c==n:
        break
    
#Q.3 Given two positive integers, compute their GCD using the Euclidean al-gorithm:
        
a=int(input('Enter the number:'))
b=int(input('entr another nmber'))

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
        
d=GCD(a,b)
print('GCD of number is:',d)


import math as m
a=int(input('Enter the number:'))
b=int(input('entr another nmber'))

d=m.gcd(a,b)
print('GCD of given no is',d)

#Q2.Write a program to compute sin(x) using the library function. The pro-gram also computes it by summing a 
nite number of terms of an in
niteseries for sin(x)

import math as m
a=m.sin(m.radians(60))
print ('vale od sin(60)',a,'ronded vale',round(a,2) )

sum=0
for i in range (-60,60,10):
    a=m.sin(m.radians(i))
    sum=sum+a
    print('vaule od sin at this degree:',i,'is',a)

print('the addition is :', sum, 'round of to 2 point is:', round(sum,2))


#Q.2Write a program to compute sin(x) using the library function. The pro-gram also computes it by summing a 
nite number of terms of an in
niteseries for sin(x)

import math as m
n=10
sin=0
c=0
for j in range(-60,60,10):
    y=m.radians(j)
    

    for i in range(n):
        sign=m.pow(-1,i)
        z=y**(2*i+1)
        f=m.factorial(2*i+1)
        sine=sign*(z/f)
        sin=sin+sine
        #print(sin)
    print(sin)
    c=c+1
    if c==10:
        break

    

    
              
          
            
    
    

