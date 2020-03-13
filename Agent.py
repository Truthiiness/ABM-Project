# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:40 2020

@author: Chris
"""

from mesa import Agent

class Agent1AA(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 100
        self.trait2 = 100
        self.trait3 = 100
        self.trait4 = 100
        self.trait5 = 100
        self.trait6 = 100
        self.trait7 = 100
        self.trait8 = 100
        self.trait9 = 100
        self.trait10 = 100
        self.trait11 = 100
        self.trait12 = 100
        
    def step(self):
        if self.trait1 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait1 += 1
            self.trait1 -= 1
        if self.trait2 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait2 += 1
            self.trait2 -= 1
        if self.trait3 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait3 += 1
            self.trait3 -= 1
        if self.trait4 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait4 += 1
            self.trait4 -= 1
        if self.trait5 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait5 += 1
            self.trait5 -= 1
        if self.trait6 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait6 += 1
            self.trait6 -= 1
        if self.trait7 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait7 += 1
            self.trait7 -= 1
        if self.trait8 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait8 += 1
            self.trait8 -= 1
        if self.trait9 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait9 += 1
            self.trait9 -= 1
        if self.trait10 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait10 += 1
            self.trait10 -= 1
        if self.trait11 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait11 += 1
            self.trait11 -= 1
        if self.trait12 >= 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            other_agent.trait12 += 1
            self.trait12 -= 1