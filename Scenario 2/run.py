# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
from Network import G
import pandas as pd

#May be replaced by identical step in Model
model = Model(len(G.nodes()))
for i in range(3650):
    model.step()

traits = model.datacollector.get_agent_vars_dataframe()
traits.to_csv("traits.csv")