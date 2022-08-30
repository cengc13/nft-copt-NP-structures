#!/usr/bin/env python3
from ase.cluster import Octahedron
from gpaw.cluster import Cluster
from ase.visualize import view
from ase.io import write, read, Trajectory
import numpy as np
from copy import copy
from testamp.utilities import enforce_magnetic_moments
from collections import Counter
from matplotlib import pyplot as plt
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

# surfaces = [(1, 0, 0), (1, 0, 0), (1, 1, 1)]
surfaces = [(1, 1, 1), (1, 1, 1), (1, 1, 1)]

# n = 3
metal = 'Pt'
# print(atomic_numbers['Co'])
# # nls = range(n,n+1)

# traj = Trajectory('1415_fully_ordered.traj', 'w')
traj = Trajectory('ptco_NPs_1pt_shell.traj', 'w')

lc = 3.936

# no_atoms_list = [43]
no_atoms_list = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]

# no_atoms = 7
alloys = ['Pt']

no_of_atoms_in_cluster  = []
EMT_time = []

length_of_atoms = []
pt_ratio = []
skin_ratio = []
for no_atoms in no_atoms_list:
    cutoff = (no_atoms - 1) // 2
    atoms = Octahedron(['Co', 'Pt'], no_atoms,
                       cutoff=cutoff,
                       # alloy=False,
                       alloy=True,
                       latticeconstant=lc)
    atoms = Cluster(positions=atoms.positions, numbers=atoms.numbers)
    # atoms.rattle(stdev=0.02)
    # atoms.rattle(stdev=0.1)
    cell = atoms.minimal_box(5., h=.18)
    atoms.set_cell(cell)
    atoms.center(vacuum=5.)
    magmom_dict = {'Pt': 0.35, 'Co': 1.91}
    atoms, skin_indices = add_skin(atoms)
    atoms = enforce_magnetic_moments(atoms, magmom_dict)
    symbols_counter = Counter(atoms.symbols)
    pt_ratio.append(symbols_counter['Pt'] / len(atoms))
    # skin_ratio.append(len(skin_indices) / len(atoms))
    length_of_atoms.append(len(atoms))
    traj.write(atoms)
