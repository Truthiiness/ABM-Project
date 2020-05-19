# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:40 2020

@author: Chris
"""

from mesa import Agent

class Org(Agent):

    node= None
    
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        
    def step(self):
        neighbor_nodes = self.model.grid.get_neighbors(self.pos, include_center=True)
        neighbors = [agent for agent in self.model.grid.get_cell_list_contents(neighbor_nodes)]
        neighbor_agents = [obj for obj in neighbors if isinstance(obj, Org)]
        if len(neighbor_agents)>0:
            other_agent = self.random.choice(neighbor_agents)
            if self.phish > 0:
                if other_agent.phish == 0:
                    return
                elif self.phish - other_agent.phish > 4:
                    other_agent.phish += 4
                elif self.phish - other_agent.phish > 0:
                    other_agent.phish = self.phish
            if self.zeroday > 0:
                if other_agent.zeroday == 0:
                    return
                elif self.zeroday - other_agent.zeroday > 4:
                    other_agent.zeroday += 4
                elif self.zeroday - other_agent.zeroday > 0:
                    other_agent.zeroday = self.zeroday
            if self.tools > 0:
                if other_agent.tools == 0:
                    return
                elif self.tools - other_agent.tools > 4:
                    other_agent.tools += 4
                elif self.tools - other_agent.tools > 0:
                    other_agent.tools = self.tools
            if self.attrib > 0:
                if other_agent.attrib == 0:
                    return
                elif self.attrib - other_agent.attrib > 4:
                    other_agent.attrib += 4
                elif self.attrib - other_agent.attrib > 0:
                    other_agent.attrib = self.attrib
            if self.stealth > 0:
                if other_agent.stealth == 0:
                    return
                elif self.stealth - other_agent.stealth > 4:
                    other_agent.stealth += 4
                elif self.stealth - other_agent.stealth > 0:
                    other_agent.stealth = self.stealth
            if self.iwo > 0:
                if other_agent.iwo == 0:
                    return
                elif self.iwo - other_agent.iwo > 4:
                    other_agent.iwo += 4
                elif self.iwo - other_agent.iwo > 0:
                    other_agent.iwo = self.iwo
            if self.ddos > 0:
                if other_agent.ddos == 0:
                    return
                elif self.ddos - other_agent.ddos > 4:
                    other_agent.ddos += 4
                elif self.ddos - other_agent.ddos > 0:
                    other_agent.ddos = self.ddos
            if self.destruct > 0:
                if other_agent.destruct == 0:
                    return
                elif self.destruct - other_agent.destruct > 4:
                    other_agent.destruct += 4
                elif self.destruct - other_agent.destruct > 0:
                    other_agent.destruct = self.destruct
            if self.infra > 0:
                if other_agent.infra == 0:
                    return
                elif self.infra - other_agent.infra > 4:
                    other_agent.infra += 4
                elif self.infra - other_agent.infra > 0:
                    other_agent.infra = self.infra
        if self.phish>0:
            self.phish += 0.5
        if self.zeroday>0:
            self.zeroday += 0.5
        if self.tools>0:
            self.tools += 0.5      
        if self.attrib>0:
            self.attrib += 0.5
        if self.stealth>0:
            self.stealth += 0.5
        if self.iwo>0:
            self.iwo += 0.5
        if self.ddos>0:
            self.ddos += 0.5
        if self.destruct>0:
            self.destruct += 0.5
        if self.infra>0:
            self.infra += 0.5

class Agent1A(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 100
        self.zeroday = 100
        self.tools = 100
        self.attrib = 100
        self.stealth = 100
        self.iwo = 0
        self.ddos = 100
        self.destruct = 100
        self.infra = 100

class Agent1B(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1

class Agent1C(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1

class Agent1D(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1
             
class Agent1E(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1
         
class Agent1F(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1

class Agent1G(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1

class Agent1H(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1

class Agent1I(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1

class Agent1J(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1

class Agent1K(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1
       
class Agent1L(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 1
        self.zeroday = 1
        self.tools = 1
        self.attrib = 1
        self.stealth = 1
        self.iwo = 1
        self.ddos = 1
        self.destruct = 1
        self.infra = 1