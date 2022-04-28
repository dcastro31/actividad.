# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:52:57 2022


"""
#Instructions ETL
"""
dict in ---> dict out
{1:'WORLD'} ---> {'world' : 1}
"""
def transform(input_dict):
        return {value.lower():key for key in input_dict for value in input_dict[key]}