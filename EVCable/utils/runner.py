#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:28:47 2019

@author: suliang
"""

class Runner():
    
    def __init__(self,cfg):
        vehicle = obj_from_dict(Vehicle, cfg.vehicle)
    
    def run(self):
        pass
    