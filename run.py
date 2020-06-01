# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
from Agent import (FancyBear, PrimitiveBear, VenomousBear, BerserkBear, CozyBear, 
                   VoodooBear, RefinedKitten, ImperialKitten, CharmingKitten, 
                   HelixKitten, StaticKitten, RemixKitten)
import numpy as np
from Network import G

#May be replaced by identical step in Model
model = Model(len(G.nodes()))
for i in range(120):
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

fancybear_phish = [a.phish for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_tools = [a.tools for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, FancyBear)]
fancybear_infra = [a.infra for a in model.schedule.agents if isinstance(a, FancyBear)]

agent1a_avg_traits = [np.mean(fancybear_phish),np.mean(fancybear_zeroday),np.mean(fancybear_tools),
np.mean(fancybear_attrib),np.mean(fancybear_stealth),np.mean(fancybear_iwo),
np.mean(fancybear_ddos),np.mean(fancybear_destruct),np.mean(fancybear_infra)]

print("Average Fancy Bear traits are:")
print(agent1a_avg_traits)

primitivebear_phish = [a.phish for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_tools = [a.tools for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, PrimitiveBear)]
primitivebear_infra = [a.infra for a in model.schedule.agents if isinstance(a, PrimitiveBear)]

agent1b_avg_traits = [np.mean(primitivebear_phish),np.mean(primitivebear_zeroday),np.mean(primitivebear_tools),
np.mean(primitivebear_attrib),np.mean(primitivebear_stealth),np.mean(primitivebear_iwo),
np.mean(primitivebear_ddos),np.mean(primitivebear_destruct),np.mean(primitivebear_infra)]

print("Average Primitive Bear traits are:") 
print(agent1b_avg_traits)

venomousbear_phish = [a.phish for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_tools = [a.tools for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, VenomousBear)]
venomousbear_infra = [a.infra for a in model.schedule.agents if isinstance(a, VenomousBear)]

agent1c_avg_traits = [np.mean(venomousbear_phish),np.mean(venomousbear_zeroday),np.mean(venomousbear_tools),
np.mean(venomousbear_attrib),np.mean(venomousbear_stealth),np.mean(venomousbear_iwo),
np.mean(venomousbear_ddos),np.mean(venomousbear_destruct),np.mean(venomousbear_infra)]

print("Average Venomous Bear traits are:")
print(agent1c_avg_traits)

berserkbear_phish = [a.phish for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_tools = [a.tools for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, BerserkBear)]
berserkbear_infra = [a.infra for a in model.schedule.agents if isinstance(a, BerserkBear)]

agent1d_avg_traits = [np.mean(berserkbear_phish),np.mean(berserkbear_zeroday),np.mean(berserkbear_tools),
np.mean(berserkbear_attrib),np.mean(berserkbear_stealth),np.mean(berserkbear_iwo),
np.mean(berserkbear_ddos),np.mean(berserkbear_destruct),np.mean(berserkbear_infra)]

print("Average Berserk Bear traits are:") 
print(agent1d_avg_traits)

cozybear_phish = [a.phish for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_tools = [a.tools for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, CozyBear)]
cozybear_infra = [a.infra for a in model.schedule.agents if isinstance(a, CozyBear)]

agent1e_avg_traits = [np.mean(cozybear_phish),np.mean(cozybear_zeroday),np.mean(cozybear_tools),
np.mean(cozybear_attrib),np.mean(cozybear_stealth),np.mean(cozybear_iwo),
np.mean(cozybear_ddos),np.mean(cozybear_destruct),np.mean(cozybear_infra)]

print("Average Cozy Bear traits are:") 
print(agent1e_avg_traits)

voodoobear_phish = [a.phish for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_tools = [a.tools for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, VoodooBear)]
voodoobear_infra = [a.infra for a in model.schedule.agents if isinstance(a, VoodooBear)]

agent1f_avg_traits = [np.mean(voodoobear_phish),np.mean(voodoobear_zeroday),np.mean(voodoobear_tools),
np.mean(voodoobear_attrib),np.mean(voodoobear_stealth),np.mean(voodoobear_iwo),
np.mean(voodoobear_ddos),np.mean(voodoobear_destruct),np.mean(voodoobear_infra)]

print("Average Voodoo Bear traits are:") 
print(agent1f_avg_traits)

refinedkitten_phish = [a.phish for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_tools = [a.tools for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, RefinedKitten)]
refinedkitten_infra = [a.infra for a in model.schedule.agents if isinstance(a, RefinedKitten)]

agent1g_avg_traits = [np.mean(refinedkitten_phish),np.mean(refinedkitten_zeroday),np.mean(refinedkitten_tools),
np.mean(refinedkitten_attrib),np.mean(refinedkitten_stealth),np.mean(refinedkitten_iwo),
np.mean(refinedkitten_ddos),np.mean(refinedkitten_destruct),np.mean(refinedkitten_infra)]

print("Average Refined Kitten traits are:")
print(agent1g_avg_traits)

imperialkitten_phish = [a.phish for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_tools = [a.tools for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, ImperialKitten)]
imperialkitten_infra = [a.infra for a in model.schedule.agents if isinstance(a, ImperialKitten)]

agent1h_avg_traits = [np.mean(imperialkitten_phish),np.mean(imperialkitten_zeroday),np.mean(imperialkitten_tools),
np.mean(imperialkitten_attrib),np.mean(imperialkitten_stealth),np.mean(imperialkitten_iwo),
np.mean(imperialkitten_ddos),np.mean(imperialkitten_destruct),np.mean(imperialkitten_infra)]

print("Average Imperial Kitten traits are:")
print(agent1h_avg_traits)

charmingkitten_phish = [a.phish for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_tools = [a.tools for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, CharmingKitten)]
charmingkitten_infra = [a.infra for a in model.schedule.agents if isinstance(a, CharmingKitten)]

agent1i_avg_traits = [np.mean(charmingkitten_phish),np.mean(charmingkitten_zeroday),np.mean(charmingkitten_tools),
np.mean(charmingkitten_attrib),np.mean(charmingkitten_stealth),np.mean(charmingkitten_iwo),
np.mean(charmingkitten_ddos),np.mean(charmingkitten_destruct),np.mean(charmingkitten_infra)]

print("Average Charming Kitten traits are:")
print(agent1i_avg_traits)

helixkitten_phish = [a.phish for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_tools = [a.tools for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, HelixKitten)]
helixkitten_infra = [a.infra for a in model.schedule.agents if isinstance(a, HelixKitten)]

agent1j_avg_traits = [np.mean(helixkitten_phish),np.mean(helixkitten_zeroday),np.mean(helixkitten_tools),
np.mean(helixkitten_attrib),np.mean(helixkitten_stealth),np.mean(helixkitten_iwo),
np.mean(helixkitten_ddos),np.mean(helixkitten_destruct),np.mean(helixkitten_infra)]

print("Average Helix Kitten traits are:")
print(agent1j_avg_traits)

statickitten_phish = [a.phish for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_tools = [a.tools for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, StaticKitten)]
statickitten_infra = [a.infra for a in model.schedule.agents if isinstance(a, StaticKitten)]

agent1k_avg_traits = [np.mean(statickitten_phish),np.mean(statickitten_zeroday),np.mean(statickitten_tools),
np.mean(statickitten_attrib),np.mean(statickitten_stealth),np.mean(statickitten_iwo),
np.mean(statickitten_ddos),np.mean(statickitten_destruct),np.mean(statickitten_infra)]

print("Average Static Kitten traits are:")
print(agent1k_avg_traits)

remixkitten_phish = [a.phish for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_zeroday = [a.zeroday for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_tools = [a.tools for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_attrib = [a.attrib for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_stealth = [a.stealth for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_iwo = [a.iwo for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_ddos = [a.ddos for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_destruct = [a.destruct for a in model.schedule.agents if isinstance(a, RemixKitten)]
remixkitten_infra = [a.infra for a in model.schedule.agents if isinstance(a, RemixKitten)]

agent1l_avg_traits = [np.mean(remixkitten_phish),np.mean(remixkitten_zeroday),np.mean(remixkitten_tools),
np.mean(remixkitten_attrib),np.mean(remixkitten_stealth),np.mean(remixkitten_iwo),
np.mean(remixkitten_ddos),np.mean(remixkitten_destruct),np.mean(remixkitten_infra)]

print("Average Remix Kitten traits are:")
print(agent1l_avg_traits)