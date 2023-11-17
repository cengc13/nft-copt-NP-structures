#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
fonts = {'size': 16}
matplotlib.rc('font', **fonts)
from ase.io import read

pre_path = '../symmetry-functions-and-trainingimages'
images = read(f'{pre_path}/trainingimages.traj', index=':')

central_forces = []
no_atoms = []
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 8))
for image in images:
	pbc = image.pbc
	if pbc.any():
		continue
	forces = image.get_forces()
	forces = ((forces ** 2).sum(axis=1))**0.5
	central_forces.append(forces[0])
	no_atoms.append(len(image))

print(np.mean(central_forces))
print(np.mean(no_atoms))
# import pickle
# with open('no_atoms.pkl', 'wb') as pf:
# 	pickle.dump(no_atoms, pf)

ax[0].hist(central_forces, bins=20, color='brown', label='atomic force')
ax[0].set_ylabel('Frequency')
ax[0].set_xlabel(r'Force on the central atom, eV/$\AA$')
ax[0].legend()
ax[1].hist(no_atoms, bins=20, color='navy', label='number of atoms')
ax[1].set_ylabel('Frequency')
ax[1].set_xlabel('Number of atoms')
ax[1].legend()
plt.tight_layout()
fig.savefig('force_and_no_atoms.pdf')
plt.show()