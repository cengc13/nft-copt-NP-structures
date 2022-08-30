#!/usr/bin/env python3
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=batch
#SBATCH --account=ap31-condo
#SBATCH --output=/dev/null
#SBATCH --mem=20g
#SBATCH --job-name=delta
from testamp.utilities import get_atomic_halfspread
from ase.io import read
import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('pdf')
font = {'size': 12}
matplotlib.rc('font', **font)

load = '../../forces.ensemble'
traj = str(os.path.split(os.getcwd())[-1])
file = f'opt_{traj}.traj'
atoms = read(file, index='-1')

index, max_hs, all_hs = get_atomic_halfspread(load=load, atoms=atoms, output=(0., 1.))
with open('delta.txt', 'w') as f:
	f.write(str(round(max(all_hs), 2)))
with open('avg_delta.txt', 'w') as f:
	f.write(str(round(np.mean(all_hs), 2)))
