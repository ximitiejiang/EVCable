#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:42:02 2019

@author: suliang
"""
size_list = [16,25,35,50]
 
class Cable():
    
    def __init__(self, size):
        assert(size in size_list, 'not valid size')
        