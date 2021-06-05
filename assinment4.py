# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:26:04 2021

@author: admin
"""
#Q.1 Create a list of the names (first names only) of 10 of your friends. 
name=['wasim','shoyab','ram','bhshan','sophia','aditya','krishna','baadal','balaji','mia']
s_name=sorted(name)
print('alphabetically sorted list is:',s_name)
startwith_b=[]
endwith_a=[]
for i in name:
    if i.startswith('b'):
        startwith_b.append(i)
    elif i.endswith('a'):
        endwith_a.append(i)
print('Name start with b is:',startwith_b)
print('Name end with a is:',endwith_a)
        
#Q.2 Q2. Create a 2-dimensional list in python named ‘mylist’ 
mylist=[[20, 53, 967, 6, 450,20, 392, 1],['If', 'I' , 'go', 'to', 'sleep', 'you', 'cannot' 'wake', 'me', 'up']]

for i in mylist[0][:]:
    if i>67:
        mylist[0].remove(i)
for i in mylist[1][:]:
    if len(i)<3:
        mylist[1].remove(i)
print(mylist)


#@3Create a list of 10 integers.
a=[-10,-22,-50,0,-4,-2,30,2,15,37]
for index,i in enumerate(a):
    if i < -10:
        a[index]=i*i      #is smaller than -10, then replace that number in the list by its square.
    
    elif i> -10 and i < 0:
        a[index]=i+100    #is between 0 and -10, then add 100 to it and rewrite in the same list.
        
for i in a[:]:            #is between 0 to 50, then duplicate that number in the list.
    if i>0 and i<50:
        a.append(i)
print(a)

#Type 2 of Q3
a=[-10,-22,-50,0,-4,-2,30,2,15,37]
for i in range(len(a)):
    if a[i]<-10:
        a[i]=a[i]*a[i]
    elif a[i]>-10 and a[i]<0:
        a[i]=a[i]+100
    elif a[i]>0 and a[i]<50:
        a.append(a[i])
        
        
print(a)
    
#Q4.

l1=[i for i in range (1,50) if i%5==0 and i%3 !=0]
print('list of element divisible by 5 but not divisible by 3.:',l1)
l2=[i for i in range (1,50) if i%7==0]
print('list of element divisible by 7:',l2)
l3=l1+l2
print('combine list:',l3)
l4=[]
for i in l3:
    if i not in l4:
        l4.append(i)
    else :
        print('elements in this new list have occurred multiple times:', i,end='')



    
    
    
    
    
    