#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 00:15:34 2023

@author: jishuhan
"""

#Input DNA sequence
seq=input("input a DNA sequence:")
#All uppercase
seq1=seq.upper()
#Create class
class  calculator (object):
    #Creation method
    def __init__ (self, DNA_seq, final_seq):
        self.DNA_seq=DNA_seq
        self.final_seq=final_seq

    def DNA(self):
        if self.final_seq > 0.5 * self.DNA_seq:
            print("protein-coding")
        elif self.final_seq < 0.1*self.DNA_seq:
            print("non-coding")
        else:
            print ("unclear")
#Define object
A=seq1.index('TGA',seq1.index('ATG'))+6
DNA1=calculator(len(seq1),A)
#Use
DNA1.DNA()