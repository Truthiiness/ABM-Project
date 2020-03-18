# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:40 2020

@author: Chris
"""

from mesa import Agent
from mesa.space import MultiGrid
from mesa.space import NetworkGrid
import networkx as nx

class Org(Agent):
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


class Agent2(Org):
    #placeholder agent for testing purposes
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 20
        self.trait2 = 20
        self.trait3 = 20
        self.trait4 = 20
        self.trait5 = 20
        self.trait6 = 20
        self.trait7 = 20
        self.trait8 = 20
        self.trait9 = 20
        self.trait10 = 20
        self.trait11 = 20
        self.trait12 = 20
        
    def step(self):
        self.move()
        if self.trait1 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait1 == 0:
                return
            elif self.trait1 - other_agent.trait1 > 4:
                other_agent.trait1 += 4
            elif self.trait1 - other_agent.trait1 > 0:
                other_agent.trait1 = self.trait1
            self.trait1 += 0.5
        if self.trait2 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait2 == 0:
                return
            elif self.trait2 - other_agent.trait2 > 4:
                other_agent.trait2 += 4
            elif self.trait2 - other_agent.trait2 > 0:
                other_agent.trait2 = self.trait2
            self.trait2 += 0.5
        if self.trait3 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait3 == 0:
                return
            elif self.trait3 - other_agent.trait3 > 4:
                other_agent.trait3 += 4
            elif self.trait3 - other_agent.trait3 > 0:
                other_agent.trait3 = self.trait3
            self.trait3 += 0.5
        if self.trait4 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait4 == 0:
                return
            elif self.trait4 - other_agent.trait4 > 4:
                other_agent.trait4 += 4
            elif self.trait4 - other_agent.trait4 > 0:
                other_agent.trait4 = self.trait4
            self.trait4 += 0.5
        if self.trait5 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait5 == 0:
                return
            elif self.trait5 - other_agent.trait5 > 4:
                other_agent.trait5 += 4
            elif self.trait5 - other_agent.trait5 > 0:
                other_agent.trait5 = self.trait5
            self.trait5 += 0.5
        if self.trait6 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait6 == 0:
                return
            elif self.trait6 - other_agent.trait6 > 4:
                other_agent.trait6 += 4
            elif self.trait6 - other_agent.trait6 > 0:
                other_agent.trait6 = self.trait6
            self.trait6 += 0.5
        if self.trait7 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait7 == 0:
                return
            elif self.trait7 - other_agent.trait7 > 4:
                other_agent.trait7 += 4
            elif self.trait7 - other_agent.trait7 > 0:
                other_agent.trait7 = self.trait7
            self.trait7 += 0.5
        if self.trait8 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait8 == 0:
                return
            elif self.trait8 - other_agent.trait8 > 4:
                other_agent.trait8 += 4
            elif self.trait8 - other_agent.trait8 > 0:
                other_agent.trait8 = self.trait8
            self.trait8 += 0.5
        if self.trait9 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait9 == 0:
                return
            elif self.trait9 - other_agent.trait9 > 4:
                other_agent.trait9 += 4
            elif self.trait9 - other_agent.trait9 > 0:
                other_agent.trait9 = self.trait9
            self.trait9 += 0.5
        if self.trait10 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait10 == 0:
                return
            elif self.trait10 - other_agent.trait10 > 4:
                other_agent.trait10 += 4
            elif self.trait10 - other_agent.trait10 > 0:
                other_agent.trait10 = self.trait10
            self.trait10 += 0.5
        if self.trait11 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait11 == 0:
                return            
            elif self.trait11 - other_agent.trait11 > 4:
                other_agent.trait11 += 4
            elif self.trait11 - other_agent.trait11 > 0:
                other_agent.trait11 = self.trait11
            self.trait11 += 0.5
        if self.trait12 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait12 == 0:
                return
            if self.trait12 - other_agent.trait12 > 4:
                other_agent.trait12 += 4
            elif self.trait12 - other_agent.trait12 > 0:
                other_agent.trait12 = self.trait12
            self.trait12 += 0.5

class Agent1A(Org):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0
        
    def step(self):
        self.move()
        if self.trait1 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait1 == 0:
                return
            elif self.trait1 - other_agent.trait1 > 4:
                other_agent.trait1 += 4
            elif self.trait1 - other_agent.trait1 > 0:
                other_agent.trait1 = self.trait1
            self.trait1 += 0.5
        if self.trait2 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait2 == 0:
                return
            elif self.trait2 - other_agent.trait2 > 4:
                other_agent.trait2 += 4
            elif self.trait2 - other_agent.trait2 > 0:
                other_agent.trait2 = self.trait2
            self.trait2 += 0.5
        if self.trait3 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait3 == 0:
                return
            elif self.trait3 - other_agent.trait3 > 4:
                other_agent.trait3 += 4
            elif self.trait3 - other_agent.trait3 > 0:
                other_agent.trait3 = self.trait3
            self.trait3 += 0.5
        if self.trait4 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait4 == 0:
                return
            elif self.trait4 - other_agent.trait4 > 4:
                other_agent.trait4 += 4
            elif self.trait4 - other_agent.trait4 > 0:
                other_agent.trait4 = self.trait4
            self.trait4 += 0.5
        if self.trait5 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait5 == 0:
                return
            elif self.trait5 - other_agent.trait5 > 4:
                other_agent.trait5 += 4
            elif self.trait5 - other_agent.trait5 > 0:
                other_agent.trait5 = self.trait5
            self.trait5 += 0.5
        if self.trait6 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait6 == 0:
                return
            elif self.trait6 - other_agent.trait6 > 4:
                other_agent.trait6 += 4
            elif self.trait6 - other_agent.trait6 > 0:
                other_agent.trait6 = self.trait6
            self.trait6 += 0.5
        if self.trait7 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait7 == 0:
                return
            elif self.trait7 - other_agent.trait7 > 4:
                other_agent.trait7 += 4
            elif self.trait7 - other_agent.trait7 > 0:
                other_agent.trait7 = self.trait7
            self.trait7 += 0.5
        if self.trait8 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait8 == 0:
                return
            elif self.trait8 - other_agent.trait8 > 4:
                other_agent.trait8 += 4
            elif self.trait8 - other_agent.trait8 > 0:
                other_agent.trait8 = self.trait8
            self.trait8 += 0.5
        if self.trait9 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait9 == 0:
                return
            elif self.trait9 - other_agent.trait9 > 4:
                other_agent.trait9 += 4
            elif self.trait9 - other_agent.trait9 > 0:
                other_agent.trait9 = self.trait9
            self.trait9 += 0.5
        if self.trait10 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait10 == 0:
                return
            elif self.trait10 - other_agent.trait10 > 4:
                other_agent.trait10 += 4
            elif self.trait10 - other_agent.trait10 > 0:
                other_agent.trait10 = self.trait10
            self.trait10 += 0.5
        if self.trait11 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait11 == 0:
                return            
            elif self.trait11 - other_agent.trait11 > 4:
                other_agent.trait11 += 4
            elif self.trait11 - other_agent.trait11 > 0:
                other_agent.trait11 = self.trait11
            self.trait11 += 0.5
        if self.trait12 > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.trait12 == 0:
                return
            if self.trait12 - other_agent.trait12 > 4:
                other_agent.trait12 += 4
            elif self.trait12 - other_agent.trait12 > 0:
                other_agent.trait12 = self.trait12
            self.trait12 += 0.5
  
# currently inactive Agents while I try to get the model to work #          
class Agent1B(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1C(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1D(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 100
        self.trait2 = 100
        self.trait3 = 100
        self.trait4 = 100
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1E(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 0
        self.trait2 = 0
        self.trait3 = 0
        self.trait4 = 0
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 100
        self.trait10 = 100
        self.trait11 = 100
        self.trait12 = 100

class Agent1F(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 0
        self.trait2 = 0
        self.trait3 = 0
        self.trait4 = 0
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 100
        self.trait10 = 100
        self.trait11 = 100
        self.trait12 = 100

class Agent1G(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 0
        self.trait2 = 0
        self.trait3 = 0
        self.trait4 = 0
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 100
        self.trait10 = 100
        self.trait11 = 100
        self.trait12 = 100

class Agent1H(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1I(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1J(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1K(Agent):
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

class Agent1L(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1M(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 100
        self.trait2 = 100
        self.trait3 = 100
        self.trait4 = 100
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 100
        self.trait10 = 100
        self.trait11 = 100
        self.trait12 = 100

class Agent1N(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1O(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 100
        self.trait2 = 100
        self.trait3 = 100
        self.trait4 = 100
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 100
        self.trait10 = 100
        self.trait11 = 100
        self.trait12 = 100

class Agent1P(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1Q(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 100
        self.trait2 = 100
        self.trait3 = 100
        self.trait4 = 100
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1R(Agent):
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
        self.trait9 = 0
        self.trait10 = 0
        self.trait11 = 0
        self.trait12 = 0

class Agent1S(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trait1 = 0
        self.trait2 = 0
        self.trait3 = 0
        self.trait4 = 0
        self.trait5 = 0
        self.trait6 = 0
        self.trait7 = 0
        self.trait8 = 0
        self.trait9 = 100
        self.trait10 = 100
        self.trait11 = 100
        self.trait12 = 100
