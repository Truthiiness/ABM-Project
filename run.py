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
    
agent_trait1 = [a.trait1 for a in model.schedule.agents]
plt.hist(agent_trait1)

agent_trait2 = [a.trait2 for a in model.schedule.agents]
plt.hist(agent_trait2)

agent_trait3 = [a.trait3 for a in model.schedule.agents]
plt.hist(agent_trait3)