# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 01:00:29 2022


"""

#Instructions Diffrence of squares
def difference_of_squares(number):
    
    return square_of_sum(number) - sum_of_squares(number)
        
def square_of_sum(number):    
    square_of_sum = sum(x for x in range(1, number+1))**2 
    
    return square_of_sum    
    
def sum_of_squares(number):
    sum_of_squares = sum(x**2 for x in range(1, number+ 1))
    
    return sum_of_squares