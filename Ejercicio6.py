# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:47:50 2022


"""

#Instrutions Leap
def leap_year(year):
    return ((year %4==0 and year %100 !=0) or (year% 400==0))