# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:39:47 2020

@author: Chris
"""

from collections import defaultdict
from mesa.time import RandomActivation

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
    
    def get_org_count(self, org_class):    
        return len(self.agents_by_org[org_class].values())