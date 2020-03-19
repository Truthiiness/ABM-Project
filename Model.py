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

#Attempt at getting just 2 different types of agents to interact using the same method as the wolf/sheep model.

class Model(Model):
    height = 20
    width = 20
    
    initial_Agent2 = 10
    initial_Agent1A = 10
    initial_Agent1B = 10
    initial_Agent1C = 10
    initial_Agent1D = 10
    initial_Agent1E = 10
    initial_Agent1F = 10
    initial_Agent1G = 10
    initial_Agent1H = 10
    initial_Agent1I = 10
    initial_Agent1J = 10
    initial_Agent1K = 10
    initial_Agent1L = 10
    initial_Agent1M = 10
    initial_Agent1N = 10
    initial_Agent1O = 10
    initial_Agent1P = 10
    initial_Agent1Q = 10
    initial_Agent1R = 10
    initial_Agent1S = 10
        
    def __init__(self, height, width, initial_Agent2=10, initial_Agent1A = 10,
                 initial_Agent1B = 10,initial_Agent1C = 10,initial_Agent1D = 10,
                 initial_Agent1E = 10,initial_Agent1F = 10,initial_Agent1G = 10,
                 initial_Agent1H = 10,initial_Agent1I = 10,initial_Agent1J = 10,
                 initial_Agent1K = 10,initial_Agent1L = 10,initial_Agent1M = 10,
                 initial_Agent1N = 10,initial_Agent1O = 10,initial_Agent1P = 10,
                 initial_Agent1Q = 10,initial_Agent1R = 10,initial_Agent1S = 10):
        super().__init__()
        self.height = height
        self.width = width
        self.initial_Agent2 = initial_Agent2
        self.initial_Agent1A = initial_Agent1A
        self.initial_Agent1B = initial_Agent1B
        self.initial_Agent1C = initial_Agent1C
        self.initial_Agent1D = initial_Agent1D
        self.initial_Agent1E = initial_Agent1E
        self.initial_Agent1F = initial_Agent1F
        self.initial_Agent1G = initial_Agent1G
        self.initial_Agent1H = initial_Agent1H
        self.initial_Agent1I = initial_Agent1I
        self.initial_Agent1J = initial_Agent1J
        self.initial_Agent1K = initial_Agent1K
        self.initial_Agent1L = initial_Agent1L
        self.initial_Agent1M = initial_Agent1M
        self.initial_Agent1N = initial_Agent1N
        self.initial_Agent1O = initial_Agent1O
        self.initial_Agent1P = initial_Agent1P
        self.initial_Agent1Q = initial_Agent1Q
        self.initial_Agent1R = initial_Agent1R
        self.initial_Agent1S = initial_Agent1S
        self.schedule = RandomActivationByOrg(self)
        self.grid = (MultiGrid(self.height, self.width, torus=True))
    
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

        for i in range(self.initial_Agent1C):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1c = Agent1C(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1c, (x,y))
            self.schedule.add(agent1c)

        for i in range(self.initial_Agent1D):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1d = Agent1D(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1d, (x,y))
            self.schedule.add(agent1d)

        for i in range(self.initial_Agent1E):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1e = Agent1E(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1e, (x,y))
            self.schedule.add(agent1e)

        for i in range(self.initial_Agent1F):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1f = Agent1F(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1f, (x,y))
            self.schedule.add(agent1f)

        for i in range(self.initial_Agent1G):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1g = Agent1G(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1g, (x,y))
            self.schedule.add(agent1g)

        for i in range(self.initial_Agent1H):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1h = Agent1H(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1h, (x,y))
            self.schedule.add(agent1h)

        for i in range(self.initial_Agent1I):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1i = Agent1I(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1i, (x,y))
            self.schedule.add(agent1i)

        for i in range(self.initial_Agent1J):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1j = Agent1J(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1j, (x,y))
            self.schedule.add(agent1j)

        for i in range(self.initial_Agent1K):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1k = Agent1K(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1k, (x,y))
            self.schedule.add(agent1k)

        for i in range(self.initial_Agent1L):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1l = Agent1L(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1l, (x,y))
            self.schedule.add(agent1l)

        for i in range(self.initial_Agent1M):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1m = Agent1M(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1m, (x,y))
            self.schedule.add(agent1m)

        for i in range(self.initial_Agent1N):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1n = Agent1N(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1n, (x,y))
            self.schedule.add(agent1n)

        for i in range(self.initial_Agent1O):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1o = Agent1O(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1o, (x,y))
            self.schedule.add(agent1o)

        for i in range(self.initial_Agent1P):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1p = Agent1P(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1p, (x,y))
            self.schedule.add(agent1p)

        for i in range(self.initial_Agent1Q):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1q = Agent1Q(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1q, (x,y))
            self.schedule.add(agent1q)

        for i in range(self.initial_Agent1R):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1r = Agent1R(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1r, (x,y))
            self.schedule.add(agent1r)

        for i in range(self.initial_Agent1S):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            agent1s = Agent1S(self.next_id(),(x,y), self, True)
            self.grid.place_agent(agent1s, (x,y))
            self.schedule.add(agent1s)
        self.running = True
        
    def step(self):       
        self.schedule.step()

    def run_model(self, step_count=10):
        for i in range(step_count):
            self.step()