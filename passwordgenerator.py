# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:59:32 2022

@author: Pierre-Henri Rossouw

60 Apps in 60 Days Challenge - App #5: Password Generator

"""


import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)