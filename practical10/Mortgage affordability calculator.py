#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:05:26 2023

@author: jishuhan
"""

#Create class
class  calculator (object):
    #Creation method
    def __init__ (self,total_value,year_salary):
        #Initialization parameter
        self.total_value=total_value
        self.year_salary=year_salary
    def new_house(self):
        if self.total_value <= 5*self.year_salary:
            print('Yes')
        else:
            print('No')
#Define object
house1 = calculator (30,7)
house2 = calculator (30,3)
#Use
house1.new_house()
house2.new_house()