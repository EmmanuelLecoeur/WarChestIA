# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:26:14 2021

@author: Emmanuel
"""

def _load_units():
    filename = '../resources/units.csv'
    try:
        units = pd.read_csv(filename, sep='\t')
    except:
        print("units.csv file was not found.")
        

_load_units()