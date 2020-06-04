# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:05:15 2020

@author: Chris
"""

from Model import Model
from Network import G

#May be replaced by identical step in Model
model = Model(len(G.nodes()))
for i in range(1):
    model.step()

traits = model.datacollector.get_agent_vars_dataframe()
is_fb = traits["Organization"]=="FancyBear"
FancyBear = traits[is_fb]
is_fb = traits["Organization"]=="PrimitiveBear"
PrimitiveBear = traits[is_fb]
is_veb = traits["Organization"]=="VenomousBear"
VenomousBear = traits[is_veb]
is_bb = traits["Organization"]=="BerserkBear"
BerserkBear = traits[is_bb]
is_cb = traits["Organization"]=="CozyBear"
CozyBear = traits[is_cb]
is_vob = traits["Organization"]=="VoodooBear"
VoodooBear = traits[is_vob]
is_rfk = traits["Organization"]=="RefinedKitten"
RefinedKitten = traits[is_rfk]
is_ik = traits["Organization"]=="ImperialKitten"
ImperialKitten = traits[is_ik]
is_ck = traits["Organization"]=="CharmingKitten"
CharmingKitten = traits[is_ck]
is_hk = traits["Organization"]=="HelixKitten"
HelixKitten = traits[is_hk]
is_sk = traits["Organization"]=="StaticKitten"
StaticKitten = traits[is_sk]
is_rmk = traits["Organization"]=="RemixKitten"
RemixKitten = traits[is_rmk]