#!/usr/bin/env python3
from ase.io import read, write
import numpy as np
from copy import copy
from collections import Counter
from matplotlib import pyplot as plt
from testamp.utilities import enforce_magnetic_moments
from ase.visualize import view

def add_skin(atoms, skin_element='Pt'):
    from ase.neighborlist import NeighborList
    Rc = 1.4 # play with Rc to find the "appropriate cn output"
    nl = NeighborList(cutoffs=Rc*np.ones(len(atoms)),
            self_interaction=False, bothways=True)
    nl.update(atoms)
    cns = []
    for _ in range(len(atoms)):
        cns.append(len(nl.get_neighbors(_)[0]))
    skin1_indices = []
    for i, atom in enumerate(atoms):
        if cns[i] < 10:
            skin1_indices.append(i)
    skin2_indices = copy(skin1_indices)
    for j in skin1_indices:
        skin2_indices.extend(nl.get_neighbors(j)[0])
    skin2_indices = list(set(skin2_indices))
    skin3_indices = copy(skin2_indices)
    for m in skin2_indices:
        skin3_indices.extend(nl.get_neighbors(m)[0])
    skin3_indices = list(set(skin3_indices))
    for k in skin1_indices:
        atoms[k].symbol = 'Pt'
    return atoms, skin2_indices


traj = read('ptco_NPs_1pt_shell.traj', index=':')

for atoms in traj:
    no_atoms = len(atoms)
    atoms, skin_indices = add_skin(atoms)
    atoms.write(f'{no_atoms}.traj')