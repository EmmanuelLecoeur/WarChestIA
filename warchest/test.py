# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:26:14 2021

@author: Emmanuel
"""

board = {(x-3, y-3, x-y) for x in range(7) for y in range(7) if abs(x-y) <=3}

def neighbors_1(x, y, z):
    res = set()
    for i in [-1, 1]:
        res.update({(x, y-i, z+i), (x+i, y+i, z), (x+i, y, z+i)})
    return {box for box in res if box in board}
    
    
def neighbors_2(x, y, z):
    res = set()
    for a, b, c in neighbors_1(x, y, z):
        res.update(neighbors_1(a, b, c))
    res.discard((x, y, z))
    return {box for box in res if box in board}