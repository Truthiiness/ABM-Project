# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
import matplotlib.pyplot as plt

model = Model(10)
for i in range(100):
    model.step()
    
agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth)

agent_value = [a.value for a in model.schedule.agents]
plt.hist(agent_value)