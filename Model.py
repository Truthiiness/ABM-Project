# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:55 2020

@author: Chris
"""

from mesa import Model
from mesa.time import RandomActivation
from collections import defaultdict
from mesa.space import NetworkGrid
from Agent import (Agent1A, Agent1B, Agent1C, Agent1D, Agent1E, Agent1F,
Agent1G, Agent1H, Agent1I, Agent1J, Agent1K, Agent1L, Agent1M, Agent1N, Agent1O,
Agent1P, Agent1Q, Agent1R, Agent1S, Agent2A)
from Network import G

#Currently random movement mirrored from the wolf/sheep model. Working on
#getting the NetworkGrid to work

class RandomActivationByOrg(RandomActivation):

    def __init__(self, model):
        super().__init__(model)
        self.agents_by_org = defaultdict(dict)

    def add(self, agent):       
        self._agents[agent.unique_id] = agent
        agent_class = type(agent)
        self.agents_by_org[agent_class][agent.unique_id] = agent

    def step(self, by_org=True):

        if by_org:
            for agent_class in self.agents_by_org:
                self.step_org(agent_class)
            self.steps += 1
            self.time += 1
        else:
            super().step()

    def step_org(self, org):
        agent_keys = list(self.agents_by_org[org].keys())
        self.model.random.shuffle(agent_keys)
        for agent_key in agent_keys:
            self.agents_by_org[org][agent_key].step()


class Model(Model):
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
    initial_Agent2A = 10
    
    def __init__(self, nodes, initial_Agent1A = 10, initial_Agent1B = 10,
                 initial_Agent1C = 10, initial_Agent1D = 10, initial_Agent1E = 10,
                 initial_Agent1F = 10, initial_Agent1G = 10, initial_Agent1H = 10,
                 initial_Agent1I = 10, initial_Agent1J = 10, initial_Agent1K = 10,
                 initial_Agent1L = 10, initial_Agent1M = 10, initial_Agent1N = 10,
                 initial_Agent1O = 10, initial_Agent1P = 10, initial_Agent1Q = 10,
                 initial_Agent1R = 10, initial_Agent1S = 10, initial_Agent2A=10):
        super().__init__()
                
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
        self.initial_Agent2A = initial_Agent2A
        
        self.grid = NetworkGrid(G)        
        self.schedule = RandomActivationByOrg(self)
                           
        for i in range(self.initial_Agent1A):
            agent1a = Agent1A(self.next_id(), 0, self)
            self.grid.place_agent(agent1a, 0)
            self.schedule.add(agent1a)

        for i in range(self.initial_Agent1B):
            agent1b = Agent1B(self.next_id(), 1, self)
            self.grid.place_agent(agent1b, 1)
            self.schedule.add(agent1b)

        for i in range(self.initial_Agent1C):
            agent1c = Agent1C(self.next_id(), 2, self)
            self.grid.place_agent(agent1c, 2)
            self.schedule.add(agent1c)

        for i in range(self.initial_Agent1D):
            agent1d = Agent1D(self.next_id(), 3, self)
            self.grid.place_agent(agent1d, 3)
            self.schedule.add(agent1d)

        for i in range(self.initial_Agent1E):
            agent1e = Agent1E(self.next_id(), 4, self)
            self.grid.place_agent(agent1e, 4)
            self.schedule.add(agent1e)

        for i in range(self.initial_Agent1F):
            agent1f = Agent1F(self.next_id(), 5, self)
            self.grid.place_agent(agent1f, 5)
            self.schedule.add(agent1f)

        for i in range(self.initial_Agent1G):
            agent1g = Agent1G(self.next_id(), 6, self)
            self.grid.place_agent(agent1g, 6)
            self.schedule.add(agent1g)

        for i in range(self.initial_Agent1H):
            agent1h = Agent1H(self.next_id(), 7, self)
            self.grid.place_agent(agent1h, 7)
            self.schedule.add(agent1h)

        for i in range(self.initial_Agent1I):
            agent1i = Agent1I(self.next_id(), 8, self)
            self.grid.place_agent(agent1i, 8)
            self.schedule.add(agent1i)

        for i in range(self.initial_Agent1J):
            agent1j = Agent1J(self.next_id(), 9, self)
            self.grid.place_agent(agent1j, 9)
            self.schedule.add(agent1j)

        for i in range(self.initial_Agent1K):
            agent1k = Agent1K(self.next_id(), 10, self)
            self.grid.place_agent(agent1k, 10)
            self.schedule.add(agent1k)

        for i in range(self.initial_Agent1L):
            agent1l = Agent1L(self.next_id(), 11, self)
            self.grid.place_agent(agent1l, 11)
            self.schedule.add(agent1l)

        for i in range(self.initial_Agent1M):
            agent1m = Agent1M(self.next_id(), 12, self)
            self.grid.place_agent(agent1m, 12)
            self.schedule.add(agent1m)

        for i in range(self.initial_Agent1N):
            agent1n = Agent1N(self.next_id(), 13, self)
            self.grid.place_agent(agent1n, 13)
            self.schedule.add(agent1n)

        for i in range(self.initial_Agent1O):
            agent1o = Agent1O(self.next_id(), 14, self)
            self.grid.place_agent(agent1o, 14)
            self.schedule.add(agent1o)

        for i in range(self.initial_Agent1P):
            agent1p = Agent1P(self.next_id(), 15, self)
            self.grid.place_agent(agent1p, 15)
            self.schedule.add(agent1p)

        for i in range(self.initial_Agent1Q):
            agent1q = Agent1Q(self.next_id(), 16, self)
            self.grid.place_agent(agent1q, 16)
            self.schedule.add(agent1q)

        for i in range(self.initial_Agent1R):
            agent1r = Agent1R(self.next_id(), 17, self)
            self.grid.place_agent(agent1r, 17)
            self.schedule.add(agent1r)

        for i in range(self.initial_Agent1S):
            agent1s = Agent1S(self.next_id(), 18, self)
            self.grid.place_agent(agent1s, 18)
            self.schedule.add(agent1s)

        for i in range(self.initial_Agent2A):
            agent2a = Agent2A(self.next_id(), 19, self)
            self.grid.place_agent(agent2a, 19)
            self.schedule.add(agent2a)
            
        self.running = True
        
    def step(self):       
        self.schedule.step()
        