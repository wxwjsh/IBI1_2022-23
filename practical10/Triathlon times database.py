#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 00:17:31 2023

@author: jishuhan
"""

#Create class
class triathlon (object):
    #Creation method
    def __init__(self,first_name,last_name,location,swim_time,cycle_time,run_time,total_time):
        #Initialization parameter
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.swim_time=swim_time
        self.cycle_time=cycle_time
        self.run_time=run_time
        self.total_time=total_time
    def Person (self):
        print('name:',self.first_name,self.last_name,', the competition took place in', self.location,', time for swim cycle and run are:',self.swim_time,self.cycle_time,self.run_time,' ','Total time:',self.total_time)
#Define object
person1=triathlon('A','B','china','50s','40s','60s','150s')
#Use
person1.Person()