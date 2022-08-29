# Optimizing Co-Pt nanoparticles via neural-network-enhanced genetic algorithms and Monte Carlo simulations

Cheng Zeng, Sushree Jagriti Sahoo, Andrew J. Medford, Andrew A. Peterson

A challenge of understanding the thermodynamic stability of Co-Pt nanoparticles is to find an appropriate inter-atomic potential.
Using a nearsighted force-training approach, we build a robust ensemble neural network (NN) potential for Co-Pt nanoparticles.
The resulting NN ensemble model shows good accuracy and transferability in describing the relative energetics for Co-Pt nanoparticles with various shapes, sizes and Co compositions.
We employ the NN potential to construct the energy convex hulls for the fcc(100), fcc(111) and a 147-atom icosahedron.
It is found that the fcc(100) surface is more likely to form a L1_0 ordered structure than the fcc(111) surface.
The energy convex hull of the icosahedron is in quantitative agreement with the one constructed by brute-force first-principles calculations.
We then apply the NN model to investigate the crossover among  structure motifs of Pt and Co-Pt nanoparticles.
Based on an empirical model, Pt truncated octahedron is the most stable shape due to its low surface and bulk energy, and a crossover between cuboctahedron and icosahedron exists at a size of 538 atoms because of the interplay of surface and bulk contribution.
A revised model is introduced to describe the role of Co alloying in the crossover for Co-Pt nanoparticles.
A crossover between icosahedron and truncated octahedron shows up, which is associated with the larger downshift of surface energy in Co-Pt icosahedron.
The larger downshift can be attributed to the strain release on the icosahedron surface due to Co alloying.
Moreover, using Monte-Carlo simulations, we attempt to find the most stable atomic arrangement for a truncated octahedron with equal Pt and Co compositions, and also we study its order-disorder phase transition.
It is demonstrated that the most stable atom arrangement is not fully L1_0 ordered, but ordered in a distinct way.
From the outermost shell to the center of a large Co-Pt truncated octahedron, the atomic arrangement follows a pattern: Pt -> Co -> L1_2(Pt_3Co) -> L1_2(PtCo_3) -> L1_0(PtCo) -> ... -> L1_0(PtCo).
Lastly, the order-disorder phase transition for a Co-Pt nanoparticle  exhibits a lower transition temperature and a smoother transition, compared to the bulk Co-Pt alloy.

<!-- arxiv preprint:  -->

The supporting data set consists of

- COh-Ih-NPs-relaxation: cuboctahedron and icosahedron nanoparticles used to generate atomic chunks.

- symmetry-functions-and-trainingimages: symmetry function files in the JSON format, training images (bulk + atomic chunks).

- ensemble models: energy and force ensemble models in JSON formats.

- ML-validation: some structure motifs created for validating ML predictions based on the work by Gruner et al. [M. E. Gruner et al. Phys. Rev. Lett., 100 (2008)]

- validation-gpaw-vs-sparc: force consistency validation between GPAW and SPARC even if GPAW used a plane-wave mode whereas SPARC used a finite-element mode.

- pt-crossover: trajectories, energetics and uncertainty results for Pt nanoparticles in various shapes.

- copt-crossover: trajectories, energetics and uncertainty results for Co-Pt nanoparticles in typical structure motifs.

- MC-vs-L10: Monte Carlo simulated putative global minima versus the fully L1_0 ordered structure: DFT  energetic comparisons.

- genetic-algorithm-db-files: ASE-db files for the genetic algorithm runs on a 80-atom fcc(100) Co-Pt surface, a 80-atom fcc(111) Co-Pt surface, and a 147-atom icosahedron Co-Pt.