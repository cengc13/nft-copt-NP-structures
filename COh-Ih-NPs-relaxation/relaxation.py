#!/usr/bin/env python3
from testamp.stats.bootstrap import BootStrap
from testamp.utilities import Logger

from ase.optimize import BFGS, MDMin
from ase.io import read

load = f'forces.ensemble'
calc = BootStrap(load, log=Logger(f'al_relaxation.log', overwrite=True))
# trajs = ['COh_Pt1415.traj', 'COh_Pt192Co68.traj',
trajs = ['COh_Pt736Co679_disordered.traj', 'COh_Pt736Co679_ordered.traj',
'COh_Pt975Co440_disordered.traj', 'Ih_Pt1150Co265.traj', 'Ih_Pt736Co679_disordered.traj',
'Ih_Pt1415.traj', 'Ih_Pt3092Co1991.traj', 'Ih_Pt3694Co1389.traj']
for traj in trajs:
	atoms = read(traj)
	filename = traj.split('.')[0]
	atoms.calc = calc
	qn = MDMin(atoms, trajectory=f'opt_{filename}.traj',
		       logfile=f'opt_{filename}.log')
	qn.run(fmax=0.05)
