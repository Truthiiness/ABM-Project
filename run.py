# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
from Agent import (Agent1A, Agent1B, Agent1C, Agent1D, Agent1E, Agent1F,
Agent1G, Agent1H, Agent1I, Agent1J, Agent1K, Agent1L, Agent1M, Agent1N, Agent1O,
Agent1P, Agent1Q, Agent1R, Agent1S, Agent2A)
import matplotlib.pyplot as plt
import numpy as np
from Network import G

#May be replaced by identical step in Model
model = Model(len(G.nodes()))
for i in range(10):
    model.step()

#Still here in case I need it later, but I don't need it at the moment. The individual
#agent traits are more useful for what I'm looking to do.

#agent_types = [a for a in model.schedule.agents_by_org]

#all_agents_trait1 = [a.trait1 for a in model.schedule.agents]
#all_agents_trait2 = [a.trait2 for a in model.schedule.agents]
#all_agents_trait3 = [a.trait3 for a in model.schedule.agents]
#all_agents_trait4 = [a.trait4 for a in model.schedule.agents]
#all_agents_trait5 = [a.trait5 for a in model.schedule.agents]
#all_agents_trait6 = [a.trait6 for a in model.schedule.agents]
#all_agents_trait7 = [a.trait7 for a in model.schedule.agents]
#all_agents_trait8 = [a.trait8 for a in model.schedule.agents]
#all_agents_trait9 = [a.trait9 for a in model.schedule.agents]
#all_agents_trait10 = [a.trait10 for a in model.schedule.agents]
#all_agents_trait11 = [a.trait11 for a in model.schedule.agents]
#all_agents_trait12 = [a.trait12 for a in model.schedule.agents]

agent1a_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1A)]

agent1a_avg_traits = [np.mean(agent1a_trait1),np.mean(agent1a_trait2),np.mean(agent1a_trait3),
np.mean(agent1a_trait4),np.mean(agent1a_trait5),np.mean(agent1a_trait6),
np.mean(agent1a_trait7),np.mean(agent1a_trait8),np.mean(agent1a_trait9),
np.mean(agent1a_trait10),np.mean(agent1a_trait11),np.mean(agent1a_trait12)]

print("Average Agent1A traits are:")
print(agent1a_avg_traits)

agent1b_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1B)]

agent1b_avg_traits = [np.mean(agent1b_trait1),np.mean(agent1b_trait2),np.mean(agent1b_trait3),
np.mean(agent1b_trait4),np.mean(agent1b_trait5),np.mean(agent1b_trait6),
np.mean(agent1b_trait7),np.mean(agent1b_trait8),np.mean(agent1b_trait9),
np.mean(agent1b_trait10),np.mean(agent1b_trait11),np.mean(agent1b_trait12)]

print("Average Agent1B traits are:") 
print(agent1b_avg_traits)

agent1c_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1C)]

agent1c_avg_traits = [np.mean(agent1c_trait1),np.mean(agent1c_trait2),np.mean(agent1c_trait3),
np.mean(agent1c_trait4),np.mean(agent1c_trait5),np.mean(agent1c_trait6),
np.mean(agent1c_trait7),np.mean(agent1c_trait8),np.mean(agent1c_trait9),
np.mean(agent1c_trait10),np.mean(agent1c_trait11),np.mean(agent1c_trait12)]

print("Average Agent1C traits are:")
print(agent1c_avg_traits)

agent1d_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1D)]

agent1d_avg_traits = [np.mean(agent1d_trait1),np.mean(agent1d_trait2),np.mean(agent1d_trait3),
np.mean(agent1d_trait4),np.mean(agent1d_trait5),np.mean(agent1d_trait6),
np.mean(agent1d_trait7),np.mean(agent1d_trait8),np.mean(agent1d_trait9),
np.mean(agent1d_trait10),np.mean(agent1d_trait11),np.mean(agent1d_trait12)]

print("Average Agent1D traits are:") 
print(agent1d_avg_traits)

agent1e_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1E)]

agent1e_avg_traits = [np.mean(agent1e_trait1),np.mean(agent1e_trait2),np.mean(agent1e_trait3),
np.mean(agent1e_trait4),np.mean(agent1e_trait5),np.mean(agent1e_trait6),
np.mean(agent1e_trait7),np.mean(agent1e_trait8),np.mean(agent1e_trait9),
np.mean(agent1e_trait10),np.mean(agent1e_trait11),np.mean(agent1e_trait12)]

print("Average Agent1E traits are:") 
print(agent1e_avg_traits)

agent1f_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1F)]

agent1f_avg_traits = [np.mean(agent1f_trait1),np.mean(agent1f_trait2),np.mean(agent1f_trait3),
np.mean(agent1f_trait4),np.mean(agent1f_trait5),np.mean(agent1f_trait6),
np.mean(agent1f_trait7),np.mean(agent1f_trait8),np.mean(agent1f_trait9),
np.mean(agent1f_trait10),np.mean(agent1f_trait11),np.mean(agent1f_trait12)]

print("Average Agent1F traits are:") 
print(agent1f_avg_traits)

agent1g_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1G)]

agent1g_avg_traits = [np.mean(agent1g_trait1),np.mean(agent1g_trait2),np.mean(agent1g_trait3),
np.mean(agent1g_trait4),np.mean(agent1g_trait5),np.mean(agent1g_trait6),
np.mean(agent1g_trait7),np.mean(agent1g_trait8),np.mean(agent1g_trait9),
np.mean(agent1g_trait10),np.mean(agent1g_trait11),np.mean(agent1g_trait12)]

print("Average Agent1G traits are:")
print(agent1g_avg_traits)

agent1h_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1H)]

agent1h_avg_traits = [np.mean(agent1h_trait1),np.mean(agent1h_trait2),np.mean(agent1h_trait3),
np.mean(agent1h_trait4),np.mean(agent1h_trait5),np.mean(agent1h_trait6),
np.mean(agent1h_trait7),np.mean(agent1h_trait8),np.mean(agent1h_trait9),
np.mean(agent1h_trait10),np.mean(agent1h_trait11),np.mean(agent1h_trait12)]

print("Average Agent1H traits are:")
print(agent1h_avg_traits)

agent1i_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1I)]

agent1i_avg_traits = [np.mean(agent1i_trait1),np.mean(agent1i_trait2),np.mean(agent1i_trait3),
np.mean(agent1i_trait4),np.mean(agent1i_trait5),np.mean(agent1i_trait6),
np.mean(agent1i_trait7),np.mean(agent1i_trait8),np.mean(agent1i_trait9),
np.mean(agent1i_trait10),np.mean(agent1i_trait11),np.mean(agent1i_trait12)]

print("Average Agent1I traits are:")
print(agent1i_avg_traits)

agent1j_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1J)]

agent1j_avg_traits = [np.mean(agent1j_trait1),np.mean(agent1j_trait2),np.mean(agent1j_trait3),
np.mean(agent1j_trait4),np.mean(agent1j_trait5),np.mean(agent1j_trait6),
np.mean(agent1j_trait7),np.mean(agent1j_trait8),np.mean(agent1j_trait9),
np.mean(agent1j_trait10),np.mean(agent1j_trait11),np.mean(agent1j_trait12)]

print("Average Agent1J traits are:")
print(agent1j_avg_traits)

agent1k_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1K)]

agent1k_avg_traits = [np.mean(agent1k_trait1),np.mean(agent1k_trait2),np.mean(agent1k_trait3),
np.mean(agent1k_trait4),np.mean(agent1k_trait5),np.mean(agent1k_trait6),
np.mean(agent1k_trait7),np.mean(agent1k_trait8),np.mean(agent1k_trait9),
np.mean(agent1k_trait10),np.mean(agent1k_trait11),np.mean(agent1k_trait12)]

print("Average Agent1K traits are:")
print(agent1k_avg_traits)

agent1l_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1L)]

agent1l_avg_traits = [np.mean(agent1l_trait1),np.mean(agent1l_trait2),np.mean(agent1l_trait3),
np.mean(agent1l_trait4),np.mean(agent1l_trait5),np.mean(agent1l_trait6),
np.mean(agent1l_trait7),np.mean(agent1l_trait8),np.mean(agent1l_trait9),
np.mean(agent1l_trait10),np.mean(agent1l_trait11),np.mean(agent1l_trait12)]

print("Average Agent1L traits are:")
print(agent1l_avg_traits)

agent1m_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1M)]
agent1m_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1M)]

agent1m_avg_traits = [np.mean(agent1m_trait1),np.mean(agent1m_trait2),np.mean(agent1m_trait3),
np.mean(agent1m_trait4),np.mean(agent1m_trait5),np.mean(agent1m_trait6),
np.mean(agent1m_trait7),np.mean(agent1m_trait8),np.mean(agent1m_trait9),
np.mean(agent1m_trait10),np.mean(agent1m_trait11),np.mean(agent1m_trait12)]

print("Average Agent1M traits are:")
print(agent1m_avg_traits)

agent1n_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1N)]
agent1n_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1N)]

agent1n_avg_traits = [np.mean(agent1n_trait1),np.mean(agent1n_trait2),np.mean(agent1n_trait3),
np.mean(agent1n_trait4),np.mean(agent1n_trait5),np.mean(agent1n_trait6),
np.mean(agent1n_trait7),np.mean(agent1n_trait8),np.mean(agent1n_trait9),
np.mean(agent1n_trait10),np.mean(agent1n_trait11),np.mean(agent1n_trait12)]

print("Average Agent1N traits are:")
print(agent1n_avg_traits)

agent1o_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1O)]
agent1o_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1O)]

agent1o_avg_traits = [np.mean(agent1o_trait1),np.mean(agent1o_trait2),np.mean(agent1o_trait3),
np.mean(agent1o_trait4),np.mean(agent1o_trait5),np.mean(agent1o_trait6),
np.mean(agent1o_trait7),np.mean(agent1o_trait8),np.mean(agent1o_trait9),
np.mean(agent1o_trait10),np.mean(agent1o_trait11),np.mean(agent1o_trait12)]

print("Average Agent1O traits are:")
print(agent1o_avg_traits)

agent1p_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1P)]
agent1p_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1P)]

agent1p_avg_traits = [np.mean(agent1p_trait1),np.mean(agent1p_trait2),np.mean(agent1p_trait3),
np.mean(agent1p_trait4),np.mean(agent1p_trait5),np.mean(agent1p_trait6),
np.mean(agent1p_trait7),np.mean(agent1p_trait8),np.mean(agent1p_trait9),
np.mean(agent1p_trait10),np.mean(agent1p_trait11),np.mean(agent1p_trait12)]

print("Average Agent1P traits are:")
print(agent1p_avg_traits)

agent1q_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1Q)]
agent1q_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1Q)]

agent1q_avg_traits = [np.mean(agent1q_trait1),np.mean(agent1q_trait2),np.mean(agent1q_trait3),
np.mean(agent1q_trait4),np.mean(agent1q_trait5),np.mean(agent1q_trait6),
np.mean(agent1q_trait7),np.mean(agent1q_trait8),np.mean(agent1q_trait9),
np.mean(agent1q_trait10),np.mean(agent1q_trait11),np.mean(agent1q_trait12)]

print("Average Agent1Q traits are:")
print(agent1q_avg_traits)

agent1r_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1R)]
agent1r_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1R)]

agent1r_avg_traits = [np.mean(agent1r_trait1),np.mean(agent1r_trait2),np.mean(agent1r_trait3),
np.mean(agent1r_trait4),np.mean(agent1r_trait5),np.mean(agent1r_trait6),
np.mean(agent1r_trait7),np.mean(agent1r_trait8),np.mean(agent1r_trait9),
np.mean(agent1r_trait10),np.mean(agent1r_trait11),np.mean(agent1r_trait12)]

print("Average Agent1R traits are:")
print(agent1r_avg_traits)

agent1s_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent1S)]
agent1s_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent1S)]

agent1s_avg_traits = [np.mean(agent1s_trait1),np.mean(agent1s_trait2),np.mean(agent1s_trait3),
np.mean(agent1s_trait4),np.mean(agent1s_trait5),np.mean(agent1s_trait6),
np.mean(agent1s_trait7),np.mean(agent1s_trait8),np.mean(agent1s_trait9),
np.mean(agent1s_trait10),np.mean(agent1s_trait11),np.mean(agent1s_trait12)]

print("Average Agent1S traits are:")
print(agent1s_avg_traits)

agent2a_trait1 = [a.trait1 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait2 = [a.trait2 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait3 = [a.trait3 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait4 = [a.trait4 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait5 = [a.trait5 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait6 = [a.trait6 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait7 = [a.trait7 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait8 = [a.trait8 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait9 = [a.trait9 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait10 = [a.trait10 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait11 = [a.trait11 for a in model.schedule.agents if isinstance(a, Agent2A)]
agent2a_trait12 = [a.trait12 for a in model.schedule.agents if isinstance(a, Agent2A)]

agent2a_avg_traits = [np.mean(agent2a_trait1),np.mean(agent2a_trait2),np.mean(agent2a_trait3),
np.mean(agent2a_trait4),np.mean(agent2a_trait5),np.mean(agent2a_trait6),
np.mean(agent2a_trait7),np.mean(agent2a_trait8),np.mean(agent2a_trait9),
np.mean(agent2a_trait10),np.mean(agent2a_trait11),np.mean(agent2a_trait12)]

print("Average Agent2A traits are:")
print(agent2a_avg_traits)