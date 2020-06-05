# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:29:08 2020

@author: Chris
"""

import networkx as nx

G = nx.Graph()

location_list = [('FB', 1), ('PB', 2), ('VEB', 3), ('BB', 4), ('CB', 5), ('VOB', 6), 
                 ('RFK', 7), ('IK', 8), ('CK', 9), ('HK', 10), ('SK', 11), ('RMK', 12)]

for loc in location_list:
    G.add_node(loc[0],location=loc[1])

permlist = [('IK', 'CK'), ('IK', 'HK'), ('HK', 'RFK'),('RMK', 'HK')]
G.add_edges_from(permlist)
