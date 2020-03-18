# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
import matplotlib.pyplot as plt

model = Model(5,5)
for i in range(10):
    model.step()

    
agent_trait1 = [a.trait1 for a in model.schedule.agents]
agent_trait2 = [a.trait2 for a in model.schedule.agents]
agent_trait3 = [a.trait3 for a in model.schedule.agents]
agent_trait4 = [a.trait4 for a in model.schedule.agents]
agent_trait5 = [a.trait5 for a in model.schedule.agents]
agent_trait6 = [a.trait6 for a in model.schedule.agents]
agent_trait7 = [a.trait7 for a in model.schedule.agents]
agent_trait8 = [a.trait8 for a in model.schedule.agents]
agent_trait9 = [a.trait9 for a in model.schedule.agents]
agent_trait10 = [a.trait10 for a in model.schedule.agents]
agent_trait11 = [a.trait11 for a in model.schedule.agents]
agent_trait12 = [a.trait12 for a in model.schedule.agents]

print(agent_trait1)