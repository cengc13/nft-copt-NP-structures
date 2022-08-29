#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
fonts = {'size': 16}
matplotlib.rc('font', **fonts)
from ase.io import read
from testamp.stats.bootstrap import BootStrap

pre_path = '../symmetry-functions-and-trainingimages'
images = read(f'{pre_path}/trainingimages.traj', index=':')
# model_forces = '../ensemble-models/forces.ensemble'
model_energy = '../ensemble-models/energy.ensemble'
# calc_f = BootStrap(load=model_forces)
calc_e = BootStrap(load=model_energy)
# central_forces = []
dft_energies = []
# all_ml_forces = []
all_ml_energies = []
# force_devs = []
# fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 8))
for image in images[:]:
	pbc = image.pbc
	if pbc.any():
		continue
	# forces = image.get_forces()
	# ml_forces = calc_f.get_forces(image)
	energy = image.get_potential_energy()
	ml_energy = calc_e.get_potential_energy(image)
	# print(energy - ml_energy)
	dft_energies.append(energy)
	all_ml_energies.append(ml_energy)
	# f_diff = (((forces - ml_forces)**2).sum(axis=1))**0.5
	# f_diff = f_diff[0]
	# forces = ((forces ** 2).sum(axis=1))**0.5
	# ml_forces = ((ml_forces ** 2).sum(axis=1))**0.5
	# central_forces.append(forces)
	# all_ml_forces.append(ml_forces)
	# print(ml_forces.shape)
	# force_devs.append(f_diff)

import pickle
# with open('dft_forces.pkl', 'wb') as pf:
# 	pickle.dump(central_forces, pf)

# with open('ml_forces.pkl', 'wb') as pf:
# 	pickle.dump(all_ml_forces, pf)

with open('dft_energies.pkl', 'wb') as pf:
	pickle.dump(dft_energies, pf)

with open('ml_energies.pkl', 'wb') as pf:
	pickle.dump(all_ml_energies, pf)

# ax[0].hist(force_devs, bins=20, color='brown', label='atomic force')
# ax[0].set_ylabel('Frequency')
# ax[0].set_xlabel(r'Force on the central atom, eV/$\AA$')
# ax[0].legend()
# # ax[1].hist(no_atoms, bins=20, color='navy', label='number of atoms')
# # ax[1].set_ylabel('Frequency')
# # ax[1].set_xlabel('Number of atoms')
# # ax[1].legend()
# plt.tight_layout()
# # fig.savefig('force_and_no_atoms.pdf')
# plt.show()