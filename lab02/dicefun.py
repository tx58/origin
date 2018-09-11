"""
A simple die roller

Author: Tianli Xia
Date: Sep 6th, 2018
"""
import random


def rollem(first,last):
    a=random.randint(first,last)
    b=random.randint(first,last)
    roll=a+b
    return roll
