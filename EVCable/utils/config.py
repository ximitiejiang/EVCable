#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 23:03:13 2019

@author: suliang
"""
from addict import Dict

class Config(Dict):
    
    def fromfile(path):
        return Dict(cfg_dict)
    

if __name__=='__main__':
    path = '../EVCable.configs.cfg_ev_nissan_leaf.py'
    cfg = Config.fromfile(path)
    