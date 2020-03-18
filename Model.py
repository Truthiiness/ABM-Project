# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:55 2020

@author: Chris
"""

from mesa import Model
from mesa.space import MultiGrid
from Agent import Agent1A, Agent2
from Scheduler import RandomActivationByOrg
from mesa.datacollection import DataCollector

#Attempt at getting just 2 different types of agents to interact using the same method as the wolf/sheep model.

class Model(Model):
    height = 20
    width = 20
    
    initial_Agent1A = 100
    initial_Agent2 = 100
        
    def __init__(self, height, width, initial_Agent1A=100, initial_Agent2=100):
        super().__init__()
        self.height = height
        self.width = width
        self.initial_Agent1A = initial_Agent1A
        self.initial_Agent2 = initial_Agent2
        self.schedule = RandomActivationByOrg(self)
        self.grid = (MultiGrid(self.height, self.width, torus=True))
        self.datacollector = DataCollector(
            {"Agent1A": lambda m: m.schedule.get_org_count(Agent1A),
             "Agent2": lambda m: m.schedule.get_org_count(Agent2)})
    
        for i in range(self.initial_Agent1A):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1a = Agent1A(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1a, (x,y))
            self.schedule.add(agent1a)

        for i in range(self.initial_Agent2):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent2 = Agent2(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent2, (x,y))
            self.schedule.add(agent2)
        
        self.running = True
        self.datacollector.collect(self)
        
    def step(self):       
        self.schedule.step()
        self.datacollector.collect(self)

    def run_model(self, step_count=10):
        for i in range(step_count):
            self.step()