#!/usr/bin/env python3
#SBATCH --account=default
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=bigmem
#SBATCH --mem=8g
#SBATCH --mail-type=end
#SBATCH --mail-user=cheng_zeng1@brown.edu
#SBATCH --job-name=ml-opt
import os
from testamp.stats.bootstrap import BootStrap
from testamp.utilities import Logger
from ase.io import read

load = '../../energy.ensemble'
calc = BootStrap(load)

traj = str(os.path.split(os.getcwd())[-1])
atoms = read(f'opt_{traj}.traj')
atoms.calc = calc
energy = atoms.get_potential_energy()
f=open('energy', 'w')
f.write(str(energy))
f.close()
