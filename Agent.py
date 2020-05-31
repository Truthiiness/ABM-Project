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
       
class Russian(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)

    def step(self):
        i=0
        while i<20:
            neighbor_nodes = self.model.grid.get_neighbors(self.pos, include_center=True)
            neighbors = [agent for agent in self.model.grid.get_cell_list_contents(neighbor_nodes)]
            neighbor_agents = [obj for obj in neighbors if isinstance(obj, Org)]        
            all_agents = [agent for agent in self.model.schedule.agents]
            iranian_agents = [obj for obj in all_agents if isinstance(obj, Iranian)]
            other_agent = self.random.choice(iranian_agents)
            if other_agent == neighbor_agents:            
                if self.phish > 0:
                    if other_agent.phish == 0:
                        return
                    elif self.phish - other_agent.phish > .06:
                        other_agent.phish += .06
                    elif self.phish - other_agent.phish > 0:
                        other_agent.phish = self.phish
                if self.zeroday > 0:
                    if other_agent.zeroday == 0:
                        return
                    elif self.zeroday - other_agent.zeroday > .06:
                        other_agent.zeroday += .06
                    elif self.zeroday - other_agent.zeroday > 0:
                        other_agent.zeroday = self.zeroday
                if self.tools > 0:
                    if other_agent.tools == 0:
                        return
                    elif self.tools - other_agent.tools > .06:
                        other_agent.tools += .06
                    elif self.tools - other_agent.tools > 0:
                        other_agent.tools = self.tools
                if self.attrib > 0:
                    if other_agent.attrib == 0:
                        return
                    elif self.attrib - other_agent.attrib > .06:
                        other_agent.attrib += .06
                    elif self.attrib - other_agent.attrib > 0:
                        other_agent.attrib = self.attrib
                if self.stealth > 0:
                    if other_agent.stealth == 0:
                        return
                    elif self.stealth - other_agent.stealth > .06:
                        other_agent.stealth += .06
                    elif self.stealth - other_agent.stealth > 0:
                        other_agent.stealth = self.stealth
                if self.iwo > 0:
                    if other_agent.iwo == 0:
                        return
                    elif self.iwo - other_agent.iwo > .06:
                        other_agent.iwo += .06
                    elif self.iwo - other_agent.iwo > 0:
                        other_agent.iwo = self.iwo
                if self.ddos > 0:
                    if other_agent.ddos == 0:
                        return
                    elif self.ddos - other_agent.ddos > .06:
                        other_agent.ddos += .06
                    elif self.ddos - other_agent.ddos > 0:
                        other_agent.ddos = self.ddos
                if self.destruct > 0:
                    if other_agent.destruct == 0:
                        return
                    elif self.destruct - other_agent.destruct > .06:
                        other_agent.destruct += .06
                    elif self.destruct - other_agent.destruct > 0:
                        other_agent.destruct = self.destruct
                if self.infra > 0:
                    if other_agent.infra == 0:
                        return
                    elif self.infra - other_agent.infra > .06:
                        other_agent.infra += .06
                    elif self.infra - other_agent.infra > 0:
                        other_agent.infra = self.infra
            else:
                if self.phish > 0:
                    if other_agent.phish == 0:
                        return
                    elif self.phish - other_agent.phish > .027:
                        other_agent.phish += .027
                    elif self.phish - other_agent.phish > 0:
                        other_agent.phish = self.phish
                if self.zeroday > 0:
                    if other_agent.zeroday == 0:
                        return
                    elif self.zeroday - other_agent.zeroday > .027:
                        other_agent.zeroday += .027
                    elif self.zeroday - other_agent.zeroday > 0:
                        other_agent.zeroday = self.zeroday
                if self.tools > 0:
                    if other_agent.tools == 0:
                        return
                    elif self.tools - other_agent.tools > .027:
                        other_agent.tools += .027
                    elif self.tools - other_agent.tools > 0:
                        other_agent.tools = self.tools
                if self.attrib > 0:
                    if other_agent.attrib == 0:
                        return
                    elif self.attrib - other_agent.attrib > .027:
                        other_agent.attrib += .027
                    elif self.attrib - other_agent.attrib > 0:
                        other_agent.attrib = self.attrib
                if self.stealth > 0:
                    if other_agent.stealth == 0:
                        return
                    elif self.stealth - other_agent.stealth > .027:
                        other_agent.stealth += .027
                    elif self.stealth - other_agent.stealth > 0:
                        other_agent.stealth = self.stealth
                if self.iwo > 0:
                    if other_agent.iwo == 0:
                        return
                    elif self.iwo - other_agent.iwo > .027:
                        other_agent.iwo += .027
                    elif self.iwo - other_agent.iwo > 0:
                        other_agent.iwo = self.iwo
                if self.ddos > 0:
                    if other_agent.ddos == 0:
                        return
                    elif self.ddos - other_agent.ddos > .027:
                        other_agent.ddos += .027
                    elif self.ddos - other_agent.ddos > 0:
                        other_agent.ddos = self.ddos
                if self.destruct > 0:
                    if other_agent.destruct == 0:
                        return
                    elif self.destruct - other_agent.destruct > .027:
                        other_agent.destruct += .027
                    elif self.destruct - other_agent.destruct > 0:
                        other_agent.destruct = self.destruct
                if self.infra > 0:
                    if other_agent.infra == 0:
                        return
                    elif self.infra - other_agent.infra > .027:
                        other_agent.infra += .027
                    elif self.infra - other_agent.infra > 0:
                        other_agent.infra = self.infra
                i+=1
        i=0
        while i<30:
            if self.phish>0:
                self.phish += 0.013
            if self.zeroday>0:
                self.zeroday += 0.013
            if self.tools>0:
                self.tools += 0.013 
            if self.attrib>0:
                self.attrib += 0.013
            if self.stealth>0:
                self.stealth += 0.013
            if self.iwo>0:
                self.iwo += 0.013
            if self.ddos>0:
                self.ddos += 0.013
            if self.destruct>0:
                self.destruct += 0.013
            if self.infra>0:
                self.infra += 0.013
            i+=1
                
class Iranian(Org):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)

    def step(self):
        i=0
        while i<30:
            neighbor_nodes = self.model.grid.get_neighbors(self.pos, include_center=True)
            neighbors = [agent for agent in self.model.grid.get_cell_list_contents(neighbor_nodes)]
            neighbor_agents = [obj for obj in neighbors if isinstance(obj, Org)]        
            all_agents = [agent for agent in self.model.schedule.agents]
            iranian_agents = [obj for obj in all_agents if isinstance(obj, Iranian)]
            other_agent = self.random.choice(iranian_agents)
            if other_agent == neighbor_agents:            
                if self.phish > 0:
                    if other_agent.phish == 0:
                        return
                    elif self.phish - other_agent.phish > .06:
                        other_agent.phish += .06
                    elif self.phish - other_agent.phish > 0:
                        other_agent.phish = self.phish
                if self.zeroday > 0:
                    if other_agent.zeroday == 0:
                        return
                    elif self.zeroday - other_agent.zeroday > .06:
                        other_agent.zeroday += .06
                    elif self.zeroday - other_agent.zeroday > 0:
                        other_agent.zeroday = self.zeroday
                if self.tools > 0:
                    if other_agent.tools == 0:
                        return
                    elif self.tools - other_agent.tools > .06:
                        other_agent.tools += .06
                    elif self.tools - other_agent.tools > 0:
                        other_agent.tools = self.tools
                if self.attrib > 0:
                    if other_agent.attrib == 0:
                        return
                    elif self.attrib - other_agent.attrib > .06:
                        other_agent.attrib += .06
                    elif self.attrib - other_agent.attrib > 0:
                        other_agent.attrib = self.attrib
                if self.stealth > 0:
                    if other_agent.stealth == 0:
                        return
                    elif self.stealth - other_agent.stealth > .06:
                        other_agent.stealth += .06
                    elif self.stealth - other_agent.stealth > 0:
                        other_agent.stealth = self.stealth
                if self.iwo > 0:
                    if other_agent.iwo == 0:
                        return
                    elif self.iwo - other_agent.iwo > .06:
                        other_agent.iwo += .06
                    elif self.iwo - other_agent.iwo > 0:
                        other_agent.iwo = self.iwo
                if self.ddos > 0:
                    if other_agent.ddos == 0:
                        return
                    elif self.ddos - other_agent.ddos > .06:
                        other_agent.ddos += .06
                    elif self.ddos - other_agent.ddos > 0:
                        other_agent.ddos = self.ddos
                if self.destruct > 0:
                    if other_agent.destruct == 0:
                        return
                    elif self.destruct - other_agent.destruct > .06:
                        other_agent.destruct += .06
                    elif self.destruct - other_agent.destruct > 0:
                        other_agent.destruct = self.destruct
                if self.infra > 0:
                    if other_agent.infra == 0:
                        return
                    elif self.infra - other_agent.infra > .06:
                        other_agent.infra += .06
                    elif self.infra - other_agent.infra > 0:
                        other_agent.infra = self.infra
            else:
                if self.phish > 0:
                    if other_agent.phish == 0:
                        return
                    elif self.phish - other_agent.phish > .027:
                        other_agent.phish += .027
                    elif self.phish - other_agent.phish > 0:
                        other_agent.phish = self.phish
                if self.zeroday > 0:
                    if other_agent.zeroday == 0:
                        return
                    elif self.zeroday - other_agent.zeroday > .027:
                        other_agent.zeroday += .027
                    elif self.zeroday - other_agent.zeroday > 0:
                        other_agent.zeroday = self.zeroday
                if self.tools > 0:
                    if other_agent.tools == 0:
                        return
                    elif self.tools - other_agent.tools > .027:
                        other_agent.tools += .027
                    elif self.tools - other_agent.tools > 0:
                        other_agent.tools = self.tools
                if self.attrib > 0:
                    if other_agent.attrib == 0:
                        return
                    elif self.attrib - other_agent.attrib > .027:
                        other_agent.attrib += .027
                    elif self.attrib - other_agent.attrib > 0:
                        other_agent.attrib = self.attrib
                if self.stealth > 0:
                    if other_agent.stealth == 0:
                        return
                    elif self.stealth - other_agent.stealth > .027:
                        other_agent.stealth += .027
                    elif self.stealth - other_agent.stealth > 0:
                        other_agent.stealth = self.stealth
                if self.iwo > 0:
                    if other_agent.iwo == 0:
                        return
                    elif self.iwo - other_agent.iwo > .027:
                        other_agent.iwo += .027
                    elif self.iwo - other_agent.iwo > 0:
                        other_agent.iwo = self.iwo
                if self.ddos > 0:
                    if other_agent.ddos == 0:
                        return
                    elif self.ddos - other_agent.ddos > .027:
                        other_agent.ddos += .027
                    elif self.ddos - other_agent.ddos > 0:
                        other_agent.ddos = self.ddos
                if self.destruct > 0:
                    if other_agent.destruct == 0:
                        return
                    elif self.destruct - other_agent.destruct > .027:
                        other_agent.destruct += .027
                    elif self.destruct - other_agent.destruct > 0:
                        other_agent.destruct = self.destruct
                if self.infra > 0:
                    if other_agent.infra == 0:
                        return
                    elif self.infra - other_agent.infra > .027:
                        other_agent.infra += .027
                    elif self.infra - other_agent.infra > 0:
                        other_agent.infra = self.infra
                i+=1
        i=0
        while i<30:
            if self.phish>0:
                self.phish += 0.013
            if self.zeroday>0:
                self.zeroday += 0.013
            if self.tools>0:
                self.tools += 0.013 
            if self.attrib>0:
                self.attrib += 0.013
            if self.stealth>0:
                self.stealth += 0.013
            if self.iwo>0:
                self.iwo += 0.013
            if self.ddos>0:
                self.ddos += 0.013
            if self.destruct>0:
                self.destruct += 0.013
            if self.infra>0:
                self.infra += 0.013
            i+=1
           
class FancyBear(Russian):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 100
        self.zeroday = 100
        self.tools = 100
        self.attrib = 100
        self.stealth = 100
        self.iwo = 100
        self.ddos = 100
        self.destruct = 100
        self.infra = 100

class PrimitiveBear(Russian):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 100
        self.zeroday = 100
        self.tools = 100
        self.attrib = 100
        self.stealth = 100
        self.iwo = 100
        self.ddos = 100
        self.destruct = 100
        self.infra = 100

class VenomousBear(Russian):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 100
        self.zeroday = 100
        self.tools = 100
        self.attrib = 100
        self.stealth = 100
        self.iwo = 100
        self.ddos = 100
        self.destruct = 100
        self.infra = 100

class BerserkBear(Russian):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 100
        self.zeroday = 100
        self.tools = 100
        self.attrib = 100
        self.stealth = 100
        self.iwo = 100
        self.ddos = 100
        self.destruct = 100
        self.infra = 100
             
class CozyBear(Russian):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 100
        self.zeroday = 100
        self.tools = 100
        self.attrib = 100
        self.stealth = 100
        self.iwo = 100
        self.ddos = 100
        self.destruct = 100
        self.infra = 100
         
class VoodooBear(Russian):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, pos, model)
        self.phish = 100
        self.zeroday = 100
        self.tools = 100
        self.attrib = 100
        self.stealth = 100
        self.iwo = 100
        self.ddos = 100
        self.destruct = 100
        self.infra = 100

class RefinedKitten(Iranian):
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

class ImperialKitten(Iranian):
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

class CharmingKitten(Iranian):
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

class HelixKitten(Iranian):
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

class StaticKitten(Iranian):
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
       
class RemixKitten(Iranian):
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