#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:04:16 2019

@author: suliang
"""

from addict import Dict

d1=Dict()
d1.a=1
d1.b=2
print(d1)

d2=Dict()
d2.a.b.c.d='hello'
print(d2)

d3=dict(a=1,b=2,c=3)
d4=Dict(d3)   # 转换以后就可以类似属性调用
print(d4.b)