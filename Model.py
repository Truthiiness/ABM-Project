# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:55 2020

@author: Chris
"""

from mesa import Model
from Agent import Agent1AA
from mesa.time import RandomActivation

class Model(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = Agent1AA(i, self)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
