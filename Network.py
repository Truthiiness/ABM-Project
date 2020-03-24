# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:29:08 2020

@author: Chris
"""

#No longer used

import networkx as nx

G = nx.Graph()

location_list = [('1A', 0), ('1B', 1), ('1C', 2), ('1D', 3), ('1E', 4), ('1F', 5), 
                 ('1G', 6), ('1H', 7), ('1I', 8), ('1J', 9), ('1K', 10), ('1L', 11), 
                 ('1M', 12), ('1N', 13), ('1O', 14), ('1P', 15), ('1Q', 16),
                 ('1R', 17), ('1S', 18), ('2A', 19)]

for loc in location_list:
    for num in range(loc[1]):  
        G.add_node(num, location = loc[0])

a1list = [('1A', '1B'), ('1A', '1C')]
G.add_edges_from(a1list)

b1list = [('1B', '1A'), ('1B', '1C')]
G.add_edges_from(b1list)

c1list = [('1C', '1A'), ('1C', '1B'), ('1C','2A')]
G.add_edges_from(c1list)

a2list = [('2A', '1C')]
G.add_edges_from(a2list)

nx.draw(G)