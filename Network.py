# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:29:08 2020

@author: Chris
"""

import networkx as nx

G = nx.Graph()

location_list = [('1A', 1), ('1B', 2), ('1C', 3), ('1D', 4), ('1E', 5), ('1F', 6), 
                 ('1G', 7), ('1H', 8), ('1I', 9), ('1J', 10), ('1K', 11), ('1L', 12), 
                 ('1M', 13), ('1N', 14), ('1O', 15), ('1P', 16), ('1Q', 17),
                 ('1R', 18), ('1S', 19), ('2A', 20)]

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
G.add_edges_from(c1list)

nx.draw(G)