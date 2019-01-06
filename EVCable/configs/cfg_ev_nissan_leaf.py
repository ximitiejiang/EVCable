#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:15:26 2019

@author: suliang
"""

# model
vehicle=dict(
    type = 'EV',
    vehicle_name = 'NissanLeaf',
    weight = 1490,
    height = 1.5,
    length = 2.5,
    width = 2.6,
    cd = 0.23,
    
    battery=dict(
        type='Battery',
        capacity=45),
    
    motor = dict(
        type='Motor',
        radium=0.85),

    drive_cycle=dict(
        type='DriveCycle',
        size=35)
)
run_config=dict(interval=0.01)




# 