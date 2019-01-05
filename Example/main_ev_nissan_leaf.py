#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:58:22 2019

@author: suliang
"""
import os,sys
from EVCable import models
from importlib import import_module

class ConfigDict():
    
    def __init__(self, cfg_dict):
        self.cfg_dict = cfg_dict
        
    def __getattr__(self, name):
        pass

def main():
    obj_type = 'Motor'    
    obj_type = getattr(models, obj_type)
    motor = obj_type()
    
    path = '../EVCable/configs/cfg_ev_nissan_leaf.py'
    path = os.path.abspath(path)
    # 加载dir
    sys.path.insert(0, os.path.dirname(path))  # 不能带地址?不能带.py?
    # 导入module
    data = import_module(os.path.basename(path)[:-3])  # data已经可以按属性访问了
    # 去除dir
    sys.path.pop(0)
    
    ConfigDict(data)
    
    
        


if __name__=='__main__':
    main()