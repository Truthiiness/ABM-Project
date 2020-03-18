# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:55 2020

@author: Chris
"""

from mesa import Model
from mesa.space import MultiGrid
from Agent import (Agent2, Agent1A, Agent1B, Agent1C, Agent1D, Agent1E, Agent1F,
Agent1G, Agent1H, Agent1I, Agent1J, Agent1K, Agent1L, Agent1M, Agent1N, Agent1O,
Agent1P, Agent1Q, Agent1R, Agent1S)
from Scheduler import RandomActivationByOrg
from mesa.datacollection import DataCollector

#Attempt at getting just 2 different types of agents to interact using the same method as the wolf/sheep model.

class Model(Model):
    height = 20
    width = 20
    
    initial_Agent2 = 10
    initial_Agent1A = 10
    initial_Agent1B = 10
        
    def __init__(self, height, width, initial_Agent2=10, initial_Agent1A = 10,
                 initial_Agent1B = 10):
        super().__init__()
        self.height = height
        self.width = width
        self.initial_Agent2 = initial_Agent2
        self.initial_Agent1A = initial_Agent1A
        self.initial_Agent1B = initial_Agent1B
        self.schedule = RandomActivationByOrg(self)
        self.grid = (MultiGrid(self.height, self.width, torus=True))
        self.datacollector = DataCollector(
            {"Agent2": lambda m: m.schedule.get_org_count(Agent2),
             "Agent1A": lambda m: m.schedule.get_org_count(Agent1A),
             "Agent1B": lambda m: m.schedule.get_org_count(Agent1B)})
    
        for i in range(self.initial_Agent2):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent2 = Agent2(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent2, (x,y))
            self.schedule.add(agent2)
            
        for i in range(self.initial_Agent1A):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1a = Agent1A(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1a, (x,y))
            self.schedule.add(agent1a)

        for i in range(self.initial_Agent1B):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1b = Agent1B(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1b, (x,y))
            self.schedule.add(agent1b)
            
        self.running = True
        self.datacollector.collect(self)
        
    def step(self):       
        self.schedule.step()
        self.datacollector.collect(self)

    def run_model(self, step_count=10):
        for i in range(step_count):
            self.step()