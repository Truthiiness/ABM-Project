# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
from Agent import (Agent1A, Agent1B, Agent1C, Agent1D, Agent1E, Agent1F,
Agent1G, Agent1H, Agent1I, Agent1J, Agent1K, Agent1L)
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

#all_agents_phish = [a.phish for a in model.schedule.agents]
#all_agents_zeroday = [a.zeroday for a in model.schedule.agents]
#all_agents_tools = [a.tools for a in model.schedule.agents]
#all_agents_attrib = [a.attrib for a in model.schedule.agents]
#all_agents_stealth = [a.stealth for a in model.schedule.agents]
#all_agents_iwo = [a.iwo for a in model.schedule.agents]
#all_agents_ddos = [a.ddos for a in model.schedule.agents]
#all_agents_destruct = [a.destruct for a in model.schedule.agents]
#all_agents_infra = [a.infra for a in model.schedule.agents]

agent1a_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1A)]
agent1a_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1A)]

agent1a_avg_traits = [np.mean(agent1a_phish),np.mean(agent1a_zeroday),np.mean(agent1a_tools),
np.mean(agent1a_attrib),np.mean(agent1a_stealth),np.mean(agent1a_iwo),
np.mean(agent1a_ddos),np.mean(agent1a_destruct),np.mean(agent1a_infra)]

print("Average Agent1A traits are:")
print(agent1a_avg_traits)

agent1b_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1B)]
agent1b_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1B)]

agent1b_avg_traits = [np.mean(agent1b_phish),np.mean(agent1b_zeroday),np.mean(agent1b_tools),
np.mean(agent1b_attrib),np.mean(agent1b_stealth),np.mean(agent1b_iwo),
np.mean(agent1b_ddos),np.mean(agent1b_destruct),np.mean(agent1b_infra)]

print("Average Agent1B traits are:") 
print(agent1b_avg_traits)

agent1c_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1C)]
agent1c_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1C)]

agent1c_avg_traits = [np.mean(agent1c_phish),np.mean(agent1c_zeroday),np.mean(agent1c_tools),
np.mean(agent1c_attrib),np.mean(agent1c_stealth),np.mean(agent1c_iwo),
np.mean(agent1c_ddos),np.mean(agent1c_destruct),np.mean(agent1c_infra)]

print("Average Agent1C traits are:")
print(agent1c_avg_traits)

agent1d_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1D)]
agent1d_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1D)]

agent1d_avg_traits = [np.mean(agent1d_phish),np.mean(agent1d_zeroday),np.mean(agent1d_tools),
np.mean(agent1d_attrib),np.mean(agent1d_stealth),np.mean(agent1d_iwo),
np.mean(agent1d_ddos),np.mean(agent1d_destruct),np.mean(agent1d_infra)]

print("Average Agent1D traits are:") 
print(agent1d_avg_traits)

agent1e_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1E)]
agent1e_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1E)]

agent1e_avg_traits = [np.mean(agent1e_phish),np.mean(agent1e_zeroday),np.mean(agent1e_tools),
np.mean(agent1e_attrib),np.mean(agent1e_stealth),np.mean(agent1e_iwo),
np.mean(agent1e_ddos),np.mean(agent1e_destruct),np.mean(agent1e_infra)]

print("Average Agent1E traits are:") 
print(agent1e_avg_traits)

agent1f_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1F)]
agent1f_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1F)]

agent1f_avg_traits = [np.mean(agent1f_phish),np.mean(agent1f_zeroday),np.mean(agent1f_tools),
np.mean(agent1f_attrib),np.mean(agent1f_stealth),np.mean(agent1f_iwo),
np.mean(agent1f_ddos),np.mean(agent1f_destruct),np.mean(agent1f_infra)]

print("Average Agent1F traits are:") 
print(agent1f_avg_traits)

agent1g_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1G)]
agent1g_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1G)]

agent1g_avg_traits = [np.mean(agent1g_phish),np.mean(agent1g_zeroday),np.mean(agent1g_tools),
np.mean(agent1g_attrib),np.mean(agent1g_stealth),np.mean(agent1g_iwo),
np.mean(agent1g_ddos),np.mean(agent1g_destruct),np.mean(agent1g_infra)]

print("Average Agent1G traits are:")
print(agent1g_avg_traits)

agent1h_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1H)]
agent1h_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1H)]

agent1h_avg_traits = [np.mean(agent1h_phish),np.mean(agent1h_zeroday),np.mean(agent1h_tools),
np.mean(agent1h_attrib),np.mean(agent1h_stealth),np.mean(agent1h_iwo),
np.mean(agent1h_ddos),np.mean(agent1h_destruct),np.mean(agent1h_infra)]

print("Average Agent1H traits are:")
print(agent1h_avg_traits)

agent1i_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1I)]
agent1i_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1I)]

agent1i_avg_traits = [np.mean(agent1i_phish),np.mean(agent1i_zeroday),np.mean(agent1i_tools),
np.mean(agent1i_attrib),np.mean(agent1i_stealth),np.mean(agent1i_iwo),
np.mean(agent1i_ddos),np.mean(agent1i_destruct),np.mean(agent1i_infra)]

print("Average Agent1I traits are:")
print(agent1i_avg_traits)

agent1j_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1J)]
agent1j_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1J)]

agent1j_avg_traits = [np.mean(agent1j_phish),np.mean(agent1j_zeroday),np.mean(agent1j_tools),
np.mean(agent1j_attrib),np.mean(agent1j_stealth),np.mean(agent1j_iwo),
np.mean(agent1j_ddos),np.mean(agent1j_destruct),np.mean(agent1j_infra)]

print("Average Agent1J traits are:")
print(agent1j_avg_traits)

agent1k_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1K)]
agent1k_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1K)]

agent1k_avg_traits = [np.mean(agent1k_phish),np.mean(agent1k_zeroday),np.mean(agent1k_tools),
np.mean(agent1k_attrib),np.mean(agent1k_stealth),np.mean(agent1k_iwo),
np.mean(agent1k_ddos),np.mean(agent1k_destruct),np.mean(agent1k_infra)]

print("Average Agent1K traits are:")
print(agent1k_avg_traits)

agent1l_phish = [a.phish for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_tools = [a.tools for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, Agent1L)]
agent1l_infra = [a.infra for a in model.schedule.agents if isinstance(a, Agent1L)]

agent1l_avg_traits = [np.mean(agent1l_phish),np.mean(agent1l_zeroday),np.mean(agent1l_tools),
np.mean(agent1l_attrib),np.mean(agent1l_stealth),np.mean(agent1l_iwo),
np.mean(agent1l_ddos),np.mean(agent1l_destruct),np.mean(agent1l_infra)]

print("Average Agent1L traits are:")
print(agent1l_avg_traits)