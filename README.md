# Phase stability of large-size nanoparticle alloy catalysts at ab initio quality using a nearsighted force-training approach

Cheng Zeng, Sushree Jagriti Sahoo, Andrew J. Medford, Andrew A. Peterson

Co–Pt
alloyed catalyst particles are integral to commercial fuel cells,
and alloyed nanoparticles are important in many applications. Such
systems are prohibitive to fully characterize with electronic structure
calculations due to their relatively large sizes of hundreds to thousands
of atoms per simulation, the huge configurational space, and the added
expense of spin-polarized calculations. Machine-learned potentials
offer a scalable solution; however, such potentials are reliable only
if representative training data can be employed, which typically also
requires large electronic structure calculations. Here, we use the
nearsighted-force training approach that allows us to make high-fidelity
machine-learned predictions on large nanoparticles with >5000 atoms
using only small and systematically generated training structures
ranging from 38 to 168 atoms. The resulting ensemble model shows good
accuracy and transferability in describing the relative energetics
for Co–Pt nanoparticles with various shapes, sizes, and Co
compositions. It is found that the fcc(100) surface is more likely
to form an L10 ordered structure than the fcc(111) surface.
The energy convex hull of a 147-atomthe icosahedron shows that the most stable
particles have Pt-rich skins and Co-rich underlayers and is in quantitative
agreement with one constructed by brute-force first-principles calculations.
Although the truncated octahedron is the most stable shape across
all studied sizes of Pt nanoparticles, a crossover to the icosahedron exists
 for CoPt nanoparticle alloys due to a large downshift of surface energy for CoPt nanoparticle alloys.
The downshift can be attributed to strain release on the icosahedral
surface due to Co alloying. We introduced a simple empirical model
to describe the role of Co alloying in the crossover for Co–Pt
nanoparticles. With Metropolis Monte Carlo simulations, we additionally
searched for the most stable atomic arrangement for a truncated octahedron
with equal Pt and Co compositions, and also we studied its order–disorder
phase transition. We validated the most stable configurations with
a new highly scalable density functional theory code called SPARC.
From the outermost shell to the center of a large Co–Pt truncated
octahedron, the atomic arrangement follows a pattern: Pt →
Co → L12(Pt3Co) → L12(PtCo3) → L10(PtCo) → ···
→ L10(PtCo). Lastly, the order–disorder phase
transition for a Co–Pt nanoparticle exhibits a lower transition
temperature and a smoother transition compared to the bulk Co–Pt
alloy.

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
