"""
A simple die roller

Author: Tianli Xia
Date: Sep 6th, 2018
"""
import random
first=1
last=6
print('Choosing two numbers between '+str(first)+ ' and '+ str(last) +'.')
a=random.randint(first,last)
b=random.randint(first,last)
roll=a+b
print("The sum is "+ str(roll) +'.')
