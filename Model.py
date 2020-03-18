# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:55 2020

@author: Chris
"""

from mesa import Model
from Agent import Agent1A, Agent2
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import networkx as nx


#Attempt at getting just 2 different types of agents to interact using the same method as the wolf/sheep model.
#Failed miserably, so just moved on to learning the networkgrid method, which is what I need anyway.
#Kept this hashed-out just in case I needed to reference it.

#from mesa.space import MultiGrid
#class Model(Model):
#    height = 20
#    width = 20
#    
#    initial_Agent1A = 100
#    initial_Agent2 = 100
#    
#    
#    def __init__(self, height, width, initial_Agent1A=100, initial_Agent2=100):
#        self.height = height
#        self.width = width
#        self.initial_Agent1A = initial_Agent1A
#        self.initial_Agent2 = initial_Agent2
#        self.schedule = RandomActivation(self)
#        self.grid = (MultiGrid(self.height, self.width, torus=True))
#    
#        for i in range(self.initial_Agent1A):
#            x = self.random.randrange(self.width)
#            y = self.random.randrange(self.height)
#            self.grid.place_agent(Agent1A, (x,y))
#            self.schedule.add(Agent1A)
#
#        for i in range(self.initial_Agent2):
#            x = self.random.randrange(self.width)
#            y = self.random.randrange(self.height)
#            self.grid.place_agent(Agent2, (x,y))
#            self.schedule.add(Agent2)
#    
#    def step(self):       
#        self.schedule.step()
#
#    def run_model(self, step_count=10):
#        for i in range(step_count):
#            self.step()