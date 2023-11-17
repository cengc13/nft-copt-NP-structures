#!/usr/bin/env python3
from amp.utilities import get_atomic_uncertainties
from ase.io import read
import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('pdf')
font = {'size': 12}
matplotlib.rc('font', **font)

load = f'forces.ensemble'
trajs = ['COh_Pt1415.traj', 'COh_Pt192Co68.traj',
'COh_Pt736Co679_disordered.traj', 'COh_Pt736Co679_ordered.traj',
'COh_Pt975Co440_disordered.traj', 'Ih_Pt1150Co265.traj', 'Ih_Pt736Co679_disordered.traj',
'Ih_Pt1415.traj', 'Ih_Pt3092Co1991.traj', 'Ih_Pt3694Co1389.traj']
for traj in trajs:
    filename = traj.split('.')[0]
    atoms = read(f'opt_{filename}.traj')
    index, max_hs, all_hs = get_atomic_uncertainties(load=load, atoms=atoms)
    with open(f'delta_{filename}.txt', 'w') as f:
        f.write(str(round(max(all_hs), 2)))
    with open(f'avg_delta_{filename}.txt', 'w') as f:
        f.write(str(round(np.mean(all_hs), 2)))
