#! /usr/bin/env python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
from matplotlib.ticker import NullFormatter, MaxNLocator, LogLocator, MultipleLocator
from itertools import product
from random import random


gs = gridspec.GridSpec(2, 1)
fig = plt.figure(figsize=(8, 8))
# plt.margins(0.5)
plt.subplots_adjust(hspace=0.45)
prepath = '../COh-Ih-NPs-relaxation'
trajs = ['COh_Pt1415.traj', 'COh_Pt192Co68.traj',
'COh_Pt736Co679_disordered.traj', 'COh_Pt736Co679_ordered.traj',
'COh_Pt975Co440_disordered.traj',
'Ih_Pt1415.traj', 'Ih_Pt1150Co265.traj', 'Ih_Pt736Co679_disordered.traj',
 'Ih_Pt3092Co1991.traj', 'Ih_Pt3694Co1389.traj']

avg_sigmas = []
N = len(trajs)
ind = np.arange(N)
width = 0.13       # the width of the bars
np.random.seed(527)
for i, traj in enumerate(trajs):
    # if i <=4:
    #     ax = plt.subplot(gs[0, 0])
    # else:
    #     i -= 4
    #     ax = plt.subplot(gs[1, 0])
    filename = traj.split('.')[0]
    with open(f'{prepath}/avg_delta_{filename}.txt', 'r') as f:
        avg_sigma = float(f.read())
    # print(avg_sigma)
    avg_sigmas.append(avg_sigma)
ind = 0.4*np.arange(1, 6)
ax = plt.subplot(gs[0, 0])
ax.bar(ind, avg_sigmas[:5], width, color='brown')
ax.set_ylim([0, 0.35])
ax.set_ylabel(r'Average atomic uncertainty, eV/\AA', fontsize=16)
# ax.xaxis.tick_top()
tick_labels = [r'COh-Pt$_{1415}$', r'COh-D-Pt$_{192}$Co$_{68}$',
               r'COh-D-Pt$_{736}$Co$_{679}$', r'COh-O-Pt$_{736}$Co$_{679}$',
               r'COh-D-Pt$_{975}$Co$_{440}$']
ax.set_xticks(ind)
ax.set_xticklabels(labels=tick_labels, rotation=0, fontsize=12)
ax.tick_params(direction='in')
plt.tick_params(axis='x', bottom='off', top='off')

ax = plt.subplot(gs[1, 0])
ax.bar(ind, avg_sigmas[5:], width, color='navy')
ax.set_ylim([0, 0.35])
ax.set_ylabel(r'Average atomic uncertainty, eV/\AA', fontsize=16)
# ax.xaxis.tick_top()
ax.set_xticks(ind)
tick_labels = [r'Ih-Pt$_{1415}$', r'Ih-D-Pt$_{1150}$Co$_{265}$',
               r'Ih-D-Pt$_{736}$Co$_{679}$', r'Ih-D-Pt$_{3092}$Co$_{1991}$',
               r'Ih-D-Pt$_{3694}$Co$_{1389}$']
ax.set_xticklabels(labels=tick_labels, rotation=0, fontsize=12)
ax.tick_params(direction='in')
plt.tick_params(axis='x', bottom='off', top='off')
# ax.legend( (bar_dict[i][0] for i in range(5)), (elementlist), fontsize=16)
plt.tight_layout()
# fig.savefig('avg_uncertainty.pdf', )
fig.savefig('_avg_uncertainty.svg')
plt.show()
