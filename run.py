# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
import matplotlib.pyplot as plt

model = Model(10)
for i in range(10):
    model.step()

