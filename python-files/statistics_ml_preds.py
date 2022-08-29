#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
fonts = {'size': 16}
matplotlib.rc('font', **fonts)
from ase.io import read
import pickle
with open('dft_forces.pkl', 'rb') as pf:
	central_forces = pickle.load(pf)

with open('ml_forces.pkl', 'rb') as pf:
	all_ml_forces = pickle.load(pf)

with open('dft_energies.pkl', 'rb') as pf:
	dft_energies = pickle.load(pf)

with open('ml_energies.pkl', 'rb') as pf:
	all_ml_energies = pickle.load(pf)

with open('no_atoms.pkl', 'rb') as pf:
	no_atoms = pickle.load(pf)

N = len(central_forces)
force_devs = []
energy_devs = []
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 8))
for ind in range(N):
	no_atom = no_atoms[ind]
	force_dev = central_forces[ind] - all_ml_forces[ind]
	force_dev = (((force_dev ** 2)).sum(axis=1)) ** 0.5
	force_devs.append(force_dev[0])
	energy_dev = dft_energies[ind] - all_ml_energies[ind]
	energy_devs.append(abs(energy_dev)/no_atom)

mae_force = np.mean(force_devs)
mae_energy = np.mean(energy_devs)
ax[0].hist(force_devs, bins=20, color='darksalmon', label='force residuals')
ax[0].text(0.3, 200, f'MAE: {mae_force:.2f} eV/$\AA$')
ax[0].set_ylabel('Frequency')
ax[0].set_xlabel(r'Force residual on the central atom, eV/$\AA$')
ax[0].legend()
ax[1].hist(energy_devs, bins=20, color='grey', label='per-atom energy residuals')
ax[1].set_ylabel('Frequency')
ax[1].text(0.015, 400, f'MAE: {mae_energy*1000:.1f} meV/atom')
ax[1].set_xlabel('Per-atom energy residual, eV')
ax[1].legend()
plt.tight_layout()
fig.savefig('ml_pred_residuals.pdf')
plt.show()