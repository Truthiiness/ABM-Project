# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
import Network
import pandas as pd
from mesa.batchrunner import BatchRunner

Russian_nodes = ['FB', 'PB', 'VEB', 'BB', 'CB', 'VOB']
Iranian_nodes = ['RFK', 'IK', 'CK', 'HK', 'SK', 'RMK']

Explist = [[('FB','RFK')],['VEB','CK'],[('PB','IK')],[('BB', 'SK')],[('VOB','RMK')],[('CB','HK')]]

num=1
model_runs = [{'G':Network.make_network(Explist[0]), 'initial_FancyBear': 1, 'initial_PrimitiveBear': 0,
    'initial_VenomousBear': 0, 'initial_BerserkBear': 0, 'initial_CozyBear': 0,
    'initial_VoodooBear': 0, 'initial_RefinedKitten': 100, 'initial_ImperialKitten': 100,
    'initial_CharmingKitten': 100, 'initial_HelixKitten': 100, 'initial_StaticKitten': 100,
    'initial_RemixKitten': 100}, 
              {'G':Network.make_network(Explist[1]), 'initial_FancyBear': 0, 'initial_PrimitiveBear': 0,
    'initial_VenomousBear': 1, 'initial_BerserkBear': 0, 'initial_CozyBear': 0,
    'initial_VoodooBear': 0, 'initial_RefinedKitten': 100, 'initial_ImperialKitten': 100,
    'initial_CharmingKitten': 100, 'initial_HelixKitten': 100, 'initial_StaticKitten': 100,
    'initial_RemixKitten': 100}, 
    {'G':Network.make_network(Explist[2]), 'initial_FancyBear': 0, 'initial_PrimitiveBear': 1,
    'initial_VenomousBear': 0, 'initial_BerserkBear': 0, 'initial_CozyBear': 0,
    'initial_VoodooBear': 0, 'initial_RefinedKitten': 100, 'initial_ImperialKitten': 100,
    'initial_CharmingKitten': 100, 'initial_HelixKitten': 100, 'initial_StaticKitten': 100,
    'initial_RemixKitten': 100}, 
    {'G':Network.make_network(Explist[3]), 'initial_FancyBear': 0, 'initial_PrimitiveBear': 0,
    'initial_VenomousBear': 0, 'initial_BerserkBear': 1, 'initial_CozyBear': 0,
    'initial_VoodooBear': 0, 'initial_RefinedKitten': 100, 'initial_ImperialKitten': 100,
    'initial_CharmingKitten': 100, 'initial_HelixKitten': 100, 'initial_StaticKitten': 100,
    'initial_RemixKitten': 100}, 
    {'G':Network.make_network(Explist[4]), 'initial_FancyBear': 0, 'initial_PrimitiveBear': 0,
    'initial_VenomousBear': 0, 'initial_BerserkBear': 0, 'initial_CozyBear': 0,
    'initial_VoodooBear': 1, 'initial_RefinedKitten': 100, 'initial_ImperialKitten': 100,
    'initial_CharmingKitten': 100, 'initial_HelixKitten': 100, 'initial_StaticKitten': 100,
    'initial_RemixKitten': 100}, 
    {'G':Network.make_network(Explist[5]), 'initial_FancyBear': 0, 'initial_PrimitiveBear': 0,
    'initial_VenomousBear': 0, 'initial_BerserkBear': 0, 'initial_CozyBear': 1,
    'initial_VoodooBear': 0, 'initial_RefinedKitten': 100, 'initial_ImperialKitten': 100,
    'initial_CharmingKitten': 100, 'initial_HelixKitten': 100, 'initial_StaticKitten': 100,
    'initial_RemixKitten': 100}]


for model_run in model_runs:
    model = Model(model_run['G'],initial_FancyBear = model_run['initial_FancyBear'], 
                  initial_PrimitiveBear = model_run['initial_PrimitiveBear'], 
                  initial_VenomousBear = model_run['initial_VenomousBear'], 
                  initial_BerserkBear = model_run['initial_BerserkBear'], 
                  initial_CozyBear = model_run['initial_CozyBear'],
                  initial_VoodooBear = model_run['initial_VoodooBear'], 
                  initial_RefinedKitten = model_run['initial_RefinedKitten'], 
                  initial_ImperialKitten = model_run['initial_ImperialKitten'], 
                  initial_CharmingKitten = model_run['initial_CharmingKitten'], 
                  initial_HelixKitten = model_run['initial_HelixKitten'], 
                  initial_StaticKitten = model_run['initial_StaticKitten'],
                  initial_RemixKitten = model_run['initial_RemixKitten'])
    
    for i in range(3650):
        model.step()
    
    traits = model.datacollector.get_agent_vars_dataframe()
    traits.to_csv("traits"+str(num)+".csv")
    num+=1
    