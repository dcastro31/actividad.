# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:32:19 2022


"""
#Instructions
#trinary

def trinary(digits):
    try:
        return int(digits, base=3)
    except ValueError:
        return 0