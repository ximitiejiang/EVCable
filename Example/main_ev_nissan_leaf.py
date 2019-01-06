#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:58:22 2019

@author: suliang
"""
import os,sys
from EVCable import models
from importlib import import_module
from addict import Dict

class ConfigDict(Dict):  # 可用于字典的便捷获取，并且适用于嵌套字典
    
    def __init__(self, cfg_dict):
        super().__init__()
        self.cfg_dict = cfg_dict
        
#    def __getattr__(self, name):
#        value = super().__getattr__(name)
#        return value
    
class Config():
    pass

def main():
    obj_type = 'Motor'    
    obj_type = getattr(models, obj_type)
    motor = obj_type()
    
    
    # 尝试实现Config功能
    path = '../EVCable/configs/cfg_ev_nissan_leaf.py'
    path = os.path.abspath(path)
    # 加载dir
    sys.path.insert(0, os.path.dirname(path))  # 不能带地址?不能带.py?
    # 导入module
    cfg = import_module(os.path.basename(path)[:-3])  
    # 去除dir
    sys.path.pop(0)
    
    print(cfg.run_config)
    print(cfg.vehicle)
#    print(cfg.battery)  # battery是嵌套在内层的dict，不能识别
    
    # cfg已经可以按属性访问了,但还是不够方便：不能识别嵌套的dict，也不能iter，也不能切片
    # 解决办法是放到addict库的Dict类中
    _cfg_dict = {
                name: value
                for name, value in cfg.__dict__.items()  #__dict__存储对象的属性
                if not name.startswith('__')             #获得属性要么切片要么从__dict__去找
                }
    cfg_dict = Dict(_cfg_dict)  # 字典数据转换为字典对象
    print(cfg_dict.vehicle.type)   # 调用字典对象的__getattr__()方法
    print(cfg_dict.vehicle.battery)
    


if __name__=='__main__':
    main()