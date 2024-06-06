# Quantum-PDE-Benchmark

Benchmark near-term quantum algorithms for Partial Differential Equations (PDEs). 

Solving PDE efficiently is important in scientific research and engineering.
Many quantum algorithms have been proposed to solve PDE on near-term quantum computers.
However, most algorithms are verified on simulators, ignoring the effect of quantum hardware noise.
This leaves the practical performance and utility of those algorithms an open question. 
We propose an effort toward filling this gap via extensive benchmarks.



Also, see this [website](https://qppqlivingreview.github.io/review/) for a brief survey of solving various PDEs with quantum algorithms.

## Install

Download all the files and finish the installation locally,

```bash
git clone https://github.com/comp-physics/Quantum-PDE-Benchmark
cd qpde-benchmark
pip install -e.
```

## Introduction

We consider the following PDEs in this benchmark with various boundary conditions.


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

1. Variational Quantum Eigensolver (VQE) 

2. Variational Quantum Linear Solver (VQLS)

3. Hamiltonian Simulation

4. Quantum Spectral Method

### Quantum Hardware

|Hardware | qubits | Quantum Volume | Speed | 1q gate error | 2q gate error| Measurement error | Vendor|
| ----------- | :-----------: |:-----------: |:-----------: |:-----------: |:-----------: |:-----------: |----------- |
|ibmq-guadalupe| 16 | 32 | 2.4k CLOPS | 3.176e-4 | 1.037e-2 | 1.795e-2 | IBM |
|ibmq-toronto  | 27 | 32 | 1.8k CLOPS | 3.064e-4 | 1.191e-2 | 2.930e-2 | IBM |
|ibmq-montreal | 27 | 128 | 2k CLOPS | 2.986e-4 | 1.168e-2 | 1.569e-2 | IBM |
|ibmq-washington| 127 | 64 | 850 CLOPS | 2.923e-4 | 1.305e-2 | 1.170e-2 | IBM |

### Tutorials

We provide tutorials to solve PDEs on IBM's superconducting quantum hardware:
1. [1D Poisson Equation using VQE](https://github.com/comp-physics/Quantum-PDE-Benchmark/blob/master/tutorials/1D_Poisson.ipynb)
2. 1D Poisson Equation using VQLS




## Copyright and License
Quantum PDE Benchmark uses Apache-2.0 license.



## Reference
[1] Peruzzo, Alberto, et al. "A variational eigenvalue solver on a photonic quantum processor." *Nature communications* 5.1 (2014): 1-7.  
[2] Bravo-Prieto, Carlos, et al. "Variational quantum linear solver." *arXiv preprint arXiv:1909.05820* (2019).  
[3] Huang, Hsin-Yuan, Kishor Bharti, and Patrick Rebentrost. "Near-term quantum algorithms for linear systems of equations." *arXiv preprint arXiv:1909.07344* (2019).

