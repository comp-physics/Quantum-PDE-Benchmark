# Quantum-PDE-Benchmark
Benchmark near-term quantum algorithms for Partial Differential Equations (PDEs).

## Install
Download all the files and finish the installation locally,

```bash
git clone https://github.com/comp-physics/Quantum-PDE-Benchmark
cd qpde-benchmark
pip install -e.
```

## Introduction


### PDE Library

The Poisson equation (elliptic)
$$
\Delta \phi = f,
$$
wave equation (hyperbolic)
$$
\partial_t^2 \phi = c^2 \Delta  \phi,
$$
heat equation (parabolic)
$$
\partial_t \phi =  \Delta  \phi,
$$
1D Reaction-diffusion equation (linear, mixed)
$$
\partial_t \phi =  D\partial_x^2\phi + f(\phi).
$$
and 1D Burgers Equation (nonlinear, mixed)
$$
\partial_t \phi =  \nu \partial_x^2\phi - \phi \partial_x \phi + f.
$$

### Quantum Solvers

### Tutorials

We provide tutorials to solve PDEs on a real quantum hardware
1. 1D Poisson Equation using VQE
1. 1D Poisson Equation using VQLS


## Copyright and License
Quantum PDE Benchmark uses Apache-2.0 license.

## Reference
[1] Peruzzo, Alberto, et al. "A variational eigenvalue solver on a photonic quantum processor." *Nature communications* 5.1 (2014): 1-7.
[2]
[3]

