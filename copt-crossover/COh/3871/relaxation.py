#!/usr/bin/env python3
#SBATCH --account=ap31-condo
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=batch
#SBATCH --mem=20g
#SBATCH --mail-type=end
#SBATCH --mail-user=cheng_zeng1@brown.edu
#SBATCH --job-name=ml-opt
import os
from testamp.stats.bootstrap import BootStrap
from testamp.utilities import Logger

from ase.io import read
from ase.optimize import BFGS, MDMin

load = '../../bootstrap.ensemble'
calc = BootStrap(load, log=Logger(f'al_relaxation.log', overwrite=True))

traj = str(os.path.split(os.getcwd())[-1])
if os.path.exists(f'opt_{traj}.traj') and os.stat(f'opt_{traj}.traj').st_size != 0:
	atoms = read(f'opt_{traj}.traj')
else:
	atoms = read(f'../{traj}.traj')
atoms.calc = calc
qn = MDMin(atoms, trajectory=f'opt_{traj}.traj', logfile=f'opt_{traj}.log')
qn.run(fmax=0.05, steps=80)
