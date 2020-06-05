# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:01:55 2020

@author: Chris
"""

from mesa import Model
from mesa.time import RandomActivation
from collections import defaultdict
from mesa.space import NetworkGrid
from Agent import (FancyBear, PrimitiveBear, VenomousBear, BerserkBear, CozyBear, 
                   VoodooBear, RefinedKitten, ImperialKitten, CharmingKitten, 
                   HelixKitten, StaticKitten, RemixKitten)
from Network import G
from mesa.datacollection import DataCollector

   
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
    initial_FancyBear = 1
    initial_PrimitiveBear = 1
    initial_VenomousBear = 1
    initial_BerserkBear = 1
    initial_CozyBear = 1
    initial_VoodooBear = 1
    initial_RefinedKitten = 100
    initial_ImperialKitten = 100
    initial_CharmingKitten = 100
    initial_HelixKitten = 100
    initial_StaticKitten = 100
    initial_RemixKitten = 100

    
    def __init__(self, nodes, initial_FancyBear = 1, initial_PrimitiveBear = 1,
                 initial_VenomousBear = 1, initial_BerserkBear = 1, initial_CozyBear = 1,
                 initial_VoodooBear = 1, initial_RefinedKitten = 100, 
                 initial_ImperialKitten = 100, initial_CharmingKitten = 100, 
                 initial_HelixKitten = 100, initial_StaticKitten = 100,
                 initial_RemixKitten = 100):
        super().__init__()
                
        self.initial_FancyBear = initial_FancyBear
        self.initial_PrimitiveBear = initial_PrimitiveBear
        self.initial_VenomousBear = initial_VenomousBear
        self.initial_BerserkBear = initial_BerserkBear
        self.initial_CozyBear = initial_CozyBear
        self.initial_VoodooBear = initial_VoodooBear
        self.initial_RefinedKitten = initial_RefinedKitten
        self.initial_ImperialKitten = initial_ImperialKitten
        self.initial_CharmingKitten = initial_CharmingKitten
        self.initial_HelixKitten = initial_HelixKitten
        self.initial_StaticKitten = initial_StaticKitten
        self.initial_RemixKitten = initial_RemixKitten

        
        self.grid = NetworkGrid(G)        
        self.schedule = RandomActivationByOrg(self)
                           
        for i in range(self.initial_FancyBear):
            fancybear = FancyBear(self.next_id(), 'FB', self)
            self.grid.place_agent(fancybear, 'FB')
            self.schedule.add(fancybear)

        for i in range(self.initial_PrimitiveBear):
            primitivebear = PrimitiveBear(self.next_id(), 'PB', self)
            self.grid.place_agent(primitivebear, 'PB')
            self.schedule.add(primitivebear)

        for i in range(self.initial_VenomousBear):
            venomousbear = VenomousBear(self.next_id(), 'VEB', self)
            self.grid.place_agent(venomousbear, 'VEB')
            self.schedule.add(venomousbear)

        for i in range(self.initial_BerserkBear):
            berserkbear = BerserkBear(self.next_id(), 'BB', self)
            self.grid.place_agent(berserkbear, 'BB')
            self.schedule.add(berserkbear)

        for i in range(self.initial_CozyBear):
            cozybear = CozyBear(self.next_id(), 'CB', self)
            self.grid.place_agent(cozybear, 'CB')
            self.schedule.add(cozybear)

        for i in range(self.initial_VoodooBear):
            voodoobear = VoodooBear(self.next_id(), 'VOB', self)
            self.grid.place_agent(voodoobear, 'VOB')
            self.schedule.add(voodoobear)

        for i in range(self.initial_RefinedKitten):
            refinedkitten = RefinedKitten(self.next_id(), 'RFK', self)
            self.grid.place_agent(refinedkitten, 'RFK')
            self.schedule.add(refinedkitten)

        for i in range(self.initial_ImperialKitten):
            imperialkitten = ImperialKitten(self.next_id(), 'IK', self)
            self.grid.place_agent(imperialkitten, 'IK')
            self.schedule.add(imperialkitten)

        for i in range(self.initial_CharmingKitten):
            charmingkitten = CharmingKitten(self.next_id(), 'CK', self)
            self.grid.place_agent(charmingkitten, 'CK')
            self.schedule.add(charmingkitten)

        for i in range(self.initial_HelixKitten):
            helixkitten = HelixKitten(self.next_id(), 'HK', self)
            self.grid.place_agent(helixkitten, 'HK')
            self.schedule.add(helixkitten)

        for i in range(self.initial_StaticKitten):
            statickitten = StaticKitten(self.next_id(), 'SK', self)
            self.grid.place_agent(statickitten, 'SK')
            self.schedule.add(statickitten)

        for i in range(self.initial_RemixKitten):
            remixkitten = RemixKitten(self.next_id(), 'RMK', self)
            self.grid.place_agent(remixkitten, 'RMK')
            self.schedule.add(remixkitten)
           
        self.running = True  
        
        self.datacollector = DataCollector(
            agent_reporters = {"Organization": "org", "Spear Phishing": "phish", "Zero Day": "zeroday",
            "Tool Sophistication": "tools", "Attribution Obfuscation": "attrib",
            "Stealth": "stealth", "Information Weaponization": "iwo","DDoS": "ddos", 
            "Data Destruction": "destruct", "Critical Infrastructure Disruption": "infra"})
        
    def step(self):       
        self.schedule.step()
        self.datacollector.collect(self)