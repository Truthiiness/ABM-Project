# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:29:08 2020

@author: Chris
"""

#No longer used

import networkx as nx

G = nx.Graph()

location_list = [('1A', 1), ('1B', 2), ('1C', 3), ('1D', 4), ('1E', 5), ('1F', 6), 
                 ('1G', 7), ('1H', 8), ('1I', 9), ('1J', 10), ('1K', 11), ('1L', 12)]
#what am I doing wrong that I need an extra empty node for this to work?

for loc in location_list:
    G.add_node(loc[0],location=loc[1])

a1list = [('1A', '1B'), ('1A', '1C'), ('1B', '1C')]
G.add_edges_from(a1list)

nx.draw(G)