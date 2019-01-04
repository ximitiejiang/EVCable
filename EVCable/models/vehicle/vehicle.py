# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from 


class Vehicle(object):
    """base class for all vehicle
    """
    __meta__ = __ABCMeta
    
    def __init__(self, cfg):
        self.weight = cfg.weight
        self.length = cfg.length
        self.width = cfg.width
        self.height = cfg.height
    
    def show_climb_curve(self):
        pass