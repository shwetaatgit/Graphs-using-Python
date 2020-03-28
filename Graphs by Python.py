'''This question is derived from the birthday paradox. Let the number of people 
in the room be n. Generate a random number between 1 and 365, n times. This simulates
n birthdays. Count how many common birthdays are present between at least two people,
and let this be denoted by c. Plot c versus n, as n varies from 1 to 366 for the
following cases:
(a) When each birthday is equally likely. c should be 2 when n is around 25 or so.
(b) When the birthdays are computed on Mars. Each Martin year is 687 days. c should 
be 2 for n around 32. 
(c) For n around 50, there is a high chance that c is at least 2. Demonstrate this
by simulating this situation 1000 times and computing the average probability. You
should get the average probability close to 0.99. This basically means that in a 
group of 50 people, you can be almost sure that two of them share the same birthday.
(d) When birthdays between 1-150 are twice as likely as 151-365
'''

#3(a,b)
import matplotlib.pyplot as plt
from random import randint

n=int(input('no. of people in a room: '))
c_value=[]
n_value=[]
for j in range(1,n+1):
    birthdays=[]
    for i in range(j):
        b=randint(1,365)
        birthdays.append(b)
    c=0
    for i in set(birthdays):
        if birthdays.count(i)>=2:
            c+=1
    c_value.append(c)
    n_value.append(j)
print(n_value,c_value)
plt.scatter(n_value,c_value)
plt.ylabel('c_value')
plt.xlabel('n_value')
plt.style.use('ggplot')
plt.show()

#3(c)
from random import randint

n=55
cc=0
for i in range(1001):
    birthdays=[]
    for i in range(n):
        b=randint(1,365)
        birthdays.append(b)
    c=0
    for i in set(birthdays):
        if birthdays.count(i)>=2:
            c+=1
    if c>=2:
        cc+=1
print(cc/1000)
   
#3(d)
import matplotlib.pyplot as plt
import random as rd
n=int(input('no. of people in a room: '))
c_value=[]
n_value=[]
for j in range(1,n+1):
    birthdays=[]
    for i in range(j):
        li = []
        b = rd.randint(1,150)
        b1 = rd.randint(1,150)
        b2 = rd.randint(151,365)
        li.extend([b,b1,b2])
        birthdays.append(rd.choice(li))
    c=0
    for i in set(birthdays):
        if birthdays.count(i)>=2:
            c+=1
    c_value.append(c)
    n_value.append(j)
print(n_value,c_value)
plt.scatter(n_value,c_value)
plt.ylabel('c_value')
plt.xlabel('n_value')
plt.style.use('ggplot')
plt.show()