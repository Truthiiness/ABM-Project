# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:29:08 2020

@author: Chris
"""

import networkx as nx

G = nx.Graph()

a1list = [('1A', '2A'), ('1A', '1B')]
G.add_edges_from(a1list)

b1list = [('1B', '1A'), ('1B', '2A')]
G.add_edges_from(b1list)

c1list = [('1C', '2A')]
G.add_edges_from(c1list)

a2list = [('2A', '1A'), ('2A', '1B'), ('2A', '1C')]
G.add_edges_from(c1list)

nx.draw(G)