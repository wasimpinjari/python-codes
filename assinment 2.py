# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:51:32 2021

@author: admin
"""
#Q.1 Write a program to add all the natural numbers that are less than 50, divisible by 5 but not divisible
sum=0
for i in range(50):
    
    if(i%5==0 and i%3!=0):
        sum=sum+i
        print('all the natural numbers that are less than 50, divisible by 5 but not divisible by 3:',sum)
      
        
#Q.3 Read a number from the user. Check if it is positive. If it is, print the square root, else tell user to provide
#positive number.
        
x= float(input('enter the no:'))
if(x > 0):
    print( 'square root is:', x**(1/2))
else:
    print('Please provide positive number')
    
#Q.4Write a program which would determine whether the  triplet can form the three sides of a triangle.

    
x=float(input('Enter the lenght of side of tringle:'))
y=float(input('Enter the lenght of side of tringle:'))
z=float(input('Enter the lenght of side of tringle:'))
if(x+y>z and y+z>x and z+x>y):
    print('Triplet can form three side of tringle')
    if(x**2==y**2+z**2 or y**2==x**2+z**2 or z**2==x**2+y**2):
        print('This is right angle tringle')
    elif(x**2 > y**2+z**2 or y**2 > x**2+z**2 or z**2 > x**2+y**2):
        print('This is obtuse angle')
    else:
        print('This is acute angle ')
        if(x==y==z):
            print('This is equilateral tringle')
        elif(x==y!=z or x==z!=y or y==z!=x):
            print('This is isosceles tringle')
        else:
            print('This is scalene tringle')
else:
    print('This will not form tringle')
                
    
# Q.2 Write a program to calculate library fine for a student. 

file1=open('library.txt','w')
name=input('Ener he name of student:')
noof_book=int(input('no of books not return:'))
dealy=int(input('Number of days delayed:'))
fine_perday=10
file1.write(str(name))
file1.write(str(noof_book))
file1.write(str(dealy))

if(dealy<10):
    lib_fine = noof_book*dealy*fine_perday
    print('library fine of for the book:',lib_fine)
elif(dealy>10 and dealy<30):
    lib_fine=2*noof_book*dealy*fine_perday
    print('library fine of for the book:',lib_fine)
else:
    dealy>30
    print('library fine is cost of book')
file1.close()       