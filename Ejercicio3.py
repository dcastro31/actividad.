# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 23:46:44 2022


"""
#Instructions Gigasecond
#Given a moment, determine the moment that would be after a 
#gigasecond has passed.

#A gigasecond is 10^9 (1,000,000,000) seconds.

import datetime
ONE_GIGASECOND = 1000000000
def add_gigasecond(date):
    return date + datetime.timedelta(0, ONE_GIGASECOND)