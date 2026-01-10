# Lecture 11: Simulation and Modeling in Neuroscience
## From Differential Equations to Multiscale Brain Models
*PhD Course in Integrative Neurosciences - Introduction to Scientific Programming*

---

## Table of Contents

1. [Introduction: What is Modeling?](#1-introduction-what-is-modeling)
2. [Types of Models](#2-types-of-models)
3. [Differential Equations Framework](#3-differential-equations-framework)
4. [Numerical Methods](#4-numerical-methods)
5. [Nonlinear Dynamics and Phase Space](#5-nonlinear-dynamics-and-phase-space)
6. [Inferring Dynamical Systems from Data](#6-inferring-dynamical-systems-from-data)
7. [Multiscale Modeling: Molecules to Behavior](#7-multiscale-modeling-molecules-to-behavior)
8. [Practical Implementation Guide](#8-practical-implementation-guide)
9. [Resources and References](#9-resources-and-references)

---

## 1. Introduction: What is Modeling?

### Definition

A **model** is a simplified representation of a system that:
- Abstracts away details to focus on essential features
- Allows us to make predictions and test hypotheses
- Bridges theory and experimental data

> *"The purpose of models is not to fit the data but to sharpen the questions."* — Samuel Karlin

### Why Model in Neuroscience?

1. **Conceptualization**: Refine questions through *in silico* hypothesis testing
2. **Formalization**: Translate concepts into equations; estimate parameters
3. **Management/Optimization**: Use validated models to improve concepts

### Essential Complexity

- Integrate rather than reduce biological complexity
- Complex systems thinking is fundamental
- Mathematical modeling is a core biomedical skill

---

## 2. Types of Models

### Model Hierarchy

```
Abstract ←――――――――――――――――――――――――――――――→ Mechanistic

Statistical   Phenomenological   Biophysical   Molecular
Models        Models            Models        Dynamics
    ↓             ↓                 ↓             ↓
Machine      Dynamical         Hodgkin-      Protein
Learning     Systems           Huxley        Folding
```

### Key Model Types

**1. Statistical Models**
- Data-driven, empirical descriptions
- Examples: GLMs, correlation analysis
- Pros: Flexible, data-efficient
- Cons: Limited mechanistic insight

**2. Phenomenological Models**
- Capture essential dynamics without full biophysics
- Examples: LIF neurons, Wilson-Cowan populations
- Pros: Computationally efficient, intuitive
- Cons: Parameter interpretation unclear

**3. Biophysical Models**
- Based on known biological mechanisms
- Examples: Hodgkin-Huxley, compartmental models
- Pros: Mechanistic understanding, predictive
- Cons: Computationally expensive, many parameters

**4. Normative Models**
- What should the system do? (optimization principles)
- Examples: Bayesian inference, efficient coding
- Pros: Principled, generalizable
- Cons: May not match biology exactly

> *"A theory has only the alternative of being right or wrong. A model has a third possibility: it may be right, but irrelevant."* — Manfred Eigen

---

## 3. Differential Equations Framework

### Why Differential Equations?

Systems of differential equations describe **every process of interest** in neuroscience: from molecules to behavior.

### Types of Differential Equations

#### Ordinary Differential Equations (ODEs)

Describe how a function of **single independent variable** (usually time) changes.

$$\frac{dx}{dt} = f(x, I)$$

**Components:**
- **x**: state variable(s) (e.g., voltage, concentration)
- **I**: input/driving force
- **f()**: function describing change
- **dx/dt**: rate of change

**Example: Hodgkin-Huxley Model**

$$C_m\dot{V} = -\bar{g}_{K} n^4 (V-E_{K}) - \bar{g}_{Na} m^3 h (V-E_{Na}) - g_L (V-E_L) + I$$

With gating variables:
$$\tau_n(V) \dot{n} = n_\infty(V)-n$$
$$\tau_m(V) \dot{m} = m_\infty(V)-m$$
$$\tau_h(V) \dot{h} = h_\infty(V)-h$$

**Key Features:**
- 4 coupled ODEs (V, n, m, h)
- Voltage-dependent rate functions
- Nonlinear dynamics
- All derivatives with respect to time only

#### Stochastic Differential Equations (SDEs)

Extend ODEs by incorporating **random noise** or stochastic fluctuations.

$$dX_t = f(X_t, t) dt + g(X_t, t) dW_t$$

**Components:**
- **f(X, t) dt**: deterministic drift (ODE part)
- **g(X, t) dW_t**: stochastic diffusion
- **dW_t**: Wiener process (Brownian motion)

**Example: Stochastic Ion Channel**

$$dN_{\text{open}} = \left[\alpha(V)(N_{\text{total}} - N_{\text{open}}) - \beta(V)N_{\text{open}}\right]dt + \sqrt{\alpha(V)(N_{\text{total}}-N_{\text{open}}) + \beta(V)N_{\text{open}}} \, dW_t$$

where:
- α(V): voltage-dependent opening rate
- β(V): voltage-dependent closing rate
- Noise scales as √N (Law of Large Numbers)

**When to Use SDEs:**
- Small populations (< 100 molecules/channels)
- Synaptic transmission variability
- Gene expression dynamics
- Single neuron spontaneous activity

#### Partial Differential Equations (PDEs)

Describe functions of **multiple independent variables** (e.g., space *and* time).

$$\frac{\partial u}{\partial t} = f\left(t, x, u, \frac{\partial u}{\partial x}, \frac{\partial^2 u}{\partial x^2}, \ldots\right)$$

**Example: Cable Equation**

$$\frac{\partial V}{\partial t} = \frac{1}{r_a C_m}\frac{\partial^2 V}{\partial x^2} - \frac{1}{C_m}\left[g_L(V - E_L) + I_{\text{ion}}(V,t)\right] + \frac{I_{\text{ext}}(x,t)}{C_m}$$

Simplified (passive cable):
$$\frac{\partial V}{\partial t} = D\frac{\partial^2 V}{\partial x^2} - \frac{V}{\tau} + I_{\text{ext}}(x,t)$$

**Applications:**
- Dendritic integration
- Axonal propagation
- Neural fields (reaction-diffusion)
- Cortical spreading waves

**Example: Reaction-Diffusion (Neural Fields)**

$$\frac{\partial u(\mathbf{x},t)}{\partial t} = D\nabla^2 u(\mathbf{x},t) + f(u(\mathbf{x},t)) + \int_{\Omega} w(\mathbf{x},\mathbf{x}')S(u(\mathbf{x}',t))d\mathbf{x}'$$

---

## 4. Numerical Methods

### The Problem

Most neural ODEs have **no analytical solution**.

Given: $\frac{dx}{dt} = f(x, I)$  
Want: $x(t) = ?$

We know the **rate of change**, but need the **trajectory**.

### Solution: Numerical Integration

Approximate solution step-by-step with discrete time steps Δt.

**Trade-offs**: accuracy vs speed vs stability

### Integration Methods

#### Forward Euler (Order 1)

$$x_{n+1} = x_n + \Delta t \cdot f(x_n, I)$$

**Properties:**
- **Simplest** method
- **Fast** (1 function evaluation per step)
- **Least accurate**
- Can be **unstable**
- Error: O(Δt)

**Python Implementation:**
```python
def euler_forward(f, y0, t, args=()):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    
    for i in range(1, n):
        dt = t[i] - t[i-1]
        y[i] = y[i-1] + dt * f(y[i-1], t[i-1], *args)
    
    return y
```

#### Runge-Kutta 2 (RK2) - Midpoint Method (Order 2)

$$k_1 = f(x_n, I)$$
$$k_2 = f(x_n + \frac{\Delta t}{2}k_1, I)$$
$$x_{n+1} = x_n + \Delta t \cdot k_2$$

**Properties:**
- **Good balance** of speed and accuracy
- **More stable** than Euler
- 2 function evaluations per step
- Error: O(Δt²)

**Python Implementation:**
```python
def rk2(f, y0, t, args=()):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    
    for i in range(1, n):
        dt = t[i] - t[i-1]
        k1 = f(y[i-1], t[i-1], *args)
        k2 = f(y[i-1] + dt/2 * k1, t[i-1] + dt/2, *args)
        y[i] = y[i-1] + dt * k2
    
    return y
```

#### Runge-Kutta 4 (RK4) (Order 4)

$$k_1 = f(x_n, I)$$
$$k_2 = f(x_n + \frac{\Delta t}{2}k_1, I)$$
$$k_3 = f(x_n + \frac{\Delta t}{2}k_2, I)$$
$$k_4 = f(x_n + \Delta t \cdot k_3, I)$$
$$x_{n+1} = x_n + \frac{\Delta t}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

**Properties:**
- **Most accurate** common method
- **Very stable**
- 4 function evaluations per step
- Weighted average of 4 slope estimates
- Error: O(Δt⁴)

**Python Implementation:**
```python
def rk4(f, y0, t, args=()):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    
    for i in range(1, n):
        dt = t[i] - t[i-1]
        k1 = f(y[i-1], t[i-1], *args)
        k2 = f(y[i-1] + dt/2 * k1, t[i-1] + dt/2, *args)
        k3 = f(y[i-1] + dt/2 * k2, t[i-1] + dt/2, *args)
        k4 = f(y[i-1] + dt * k3, t[i-1] + dt, *args)
        y[i] = y[i-1] + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return y
```

### Practical Guidelines

**Choosing Time Step:**
$$\Delta t \leq \frac{\tau_{\text{fastest}}}{10}$$

where τ_fastest is the smallest time constant in your system.

**Method Selection:**

| Model Type | Recommended Method | Typical Δt |
|------------|-------------------|-----------|
| LIF neurons | RK4 | τ_m/10 (1-2 ms) |
| HH neurons | RK4 or adaptive | 0.01-0.1 ms |
| Networks | Euler (efficiency) | 0.01-0.1 ms |
| Stiff systems | Implicit (BDF, Radau) | adaptive |

**Error Accumulation:**
- Euler with large Δt: Fast but accumulates error, may miss spikes
- RK4 or smaller Δt: Accurate spike timing, higher cost
- Adaptive stepping: Adjust Δt based on local error (optimal efficiency)

### Crank-Nicolson Method (for PDEs)

An **implicit** scheme for parabolic PDEs (like the cable equation):

$$\frac{V^{n+1}_i - V^n_i}{\Delta t} = \frac{1}{2}\left[D\frac{\partial^2 V^{n+1}}{\partial x^2} + D\frac{\partial^2 V^{n}}{\partial x^2}\right] - \frac{1}{2\tau}(V^{n+1}_i + V^n_i) + I$$

**Properties:**
- **Unconditionally stable** (can use larger Δt)
- 2nd order accurate in time and space
- Requires solving **tridiagonal linear system** at each step
- Use `scipy.sparse.linalg.spsolve` for efficiency

---

## 5. Nonlinear Dynamics and Phase Space

### Dynamics: The Study of Change

Given: $\frac{dx}{dt} = f(x, I)$

### Fixed Points

A **fixed point** is a state where the system doesn't change:

$$f(x^*, I) = 0 \quad \Longrightarrow \quad \frac{dx}{dt} = 0$$

**Types:**
- **Stable fixed point** (attractor): system converges to it
- **Unstable fixed point** (repeller): system diverges from it
- **Saddle point**: attracts in some directions, repels in others

### Stability Analysis

Linearize around fixed point x*:
$$\frac{dx}{dt} \approx J(x^*) \cdot (x - x^*)$$

where J is the Jacobian matrix.

**Stability determined by eigenvalues λ:**
- All Re(λ) < 0: **Stable**
- Any Re(λ) > 0: **Unstable**
- Re(λ) = 0: **Bifurcation point**

### Phase Space (State Space)

The **phase space** is the space spanned by all dynamical variables (all possible states).

**Key Concepts:**

**1. Trajectories (Orbits)**
- Each point represents one state (e.g., V, dV/dt)
- System evolution = trajectory through space
- Initial condition determines trajectory

**2. Vector Field (Flow Field)**
- At each point, arrows show direction of change
- Magnitude indicates speed of change
- Trajectories follow vector field

**3. Nullclines**
- Curves where one derivative is zero
- Intersection of nullclines = fixed point
- Use to sketch phase portraits

**4. Attractors**
- **Point attractor**: rest state
- **Limit cycle**: oscillations (closed orbit)
- **Strange attractor**: chaos
- **Manifold attractor**: continuous attraction domain

### Bifurcations

Points in parameter space where **qualitative changes** in dynamics occur.

**Common Bifurcations in Neuroscience:**

**1. Saddle-Node Bifurcation**
- Two fixed points collide and annihilate
- Transitions between rest and repetitive firing
- Example: Type I excitability

**2. Hopf Bifurcation**
- Fixed point loses stability, limit cycle emerges
- Onset of oscillations
- Example: Type II excitability

**3. Saddle-Node on Invariant Circle (SNIC)**
- Bifurcation on limit cycle
- Very slow spike initiation

### Example: 2D Neural Model

$$\frac{dV}{dt} = -\left(17.81+47.58V+33.8V^2\right)(V-0.48) - 26R(V+0.95) + I$$
$$\frac{dR}{dt} = \frac{-R+1.29V+0.79+0.33(V+0.38)^2}{\tau_R}$$

**Analysis Steps:**
1. Find fixed points: set dV/dt = 0, dR/dt = 0
2. Plot nullclines
3. Determine stability (Jacobian eigenvalues)
4. Sketch phase portrait
5. Identify attractor type

---

## 6. Inferring Dynamical Systems from Data

### The Inverse Problem

Given:
- Observations (finite, noisy, incomplete)
- No knowledge of governing equations

Want:
- Understand system behavior
- Infer system equations

### Recurrent Neural Networks as Universal Approximators

**Key Theorem**: RNNs can approximate **any nonlinear dynamical system** to arbitrary precision.

$$\mathbf{z}_t = \mathbf{F}_\theta(\mathbf{z}_{t-1}, \mathbf{s}_t)$$

General form:
$$\mathbf{z}_{t} = \mathbf{A} \mathbf{z}_{t-1} + \mathbf{W} \phi(\mathbf{z}_{t-1}) + \mathbf{C} \mathbf{s}_{t}$$

**Goal**: Generate models that produce trajectories with:
- **Topological structure** matching true system
- **Geometrical properties** preserved
- **Long-term temporal signatures** consistent

### Example: Lorenz Attractor Reconstruction

True system (stochastic):
$$dx = (\sigma(y-x)) dt + d\epsilon_1(t)$$
$$dy = (x(\rho-z)-y) dt + d\epsilon_2(t)$$
$$dz = (xy-\beta z) dt + d\epsilon_3(t)$$

RNN approximation:
$$\mathbf{z}_t = \mathbf{A} \mathbf{z}_{t-1} + \mathbf{W} \phi(\mathbf{z}_{t-1}) + \mathbf{C} \mathbf{s}_t$$

**Key Insight**: Mathematical form can be completely different from underlying system, yet capture same dynamics!

### Sparse Identification of Nonlinear Dynamics (SINDy)

Alternative approach: Directly infer equation form.

1. Construct library of candidate functions
2. Use sparse regression to identify active terms
3. Validate reconstructed system

**Advantages:**
- Interpretable equations
- Fewer parameters than RNN

**Limitations:**
- Requires dense sampling
- Sensitive to noise
- Library must contain true terms

### Applications

- **fMRI/EEG data**: Reconstruct brain dynamics
- **Neural recordings**: Infer population dynamics
- **Behavioral data**: Model cognitive processes
- **Bursting neurons**: Reproduce complex spiking patterns

---

## 7. Multiscale Modeling: Molecules to Behavior

### Scale Hierarchy

```
Molecular    →    Cellular    →    Network    →    Systems
(nm, ps)         (μm, ms)         (mm, ms)        (cm, s)
   ↓                 ↓                ↓               ↓
Docking         Hodgkin-Huxley   Wilson-Cowan   Whole-brain
MD              Compartmental     Mean-field      Digital twins
```

### Molecular Scale: Docking and Dynamics

**Molecular Docking** (Static):
- Find binding poses
- Estimate binding affinity ΔG
- Drug discovery screening

**Molecular Dynamics** (Dynamic):
- Trajectories over time
- Newton's equations
- Mechanistic insight

**Bridge to Mesoscale:**
$$k_d = \frac{k_{\text{off}}}{k_{\text{on}}} = \exp(\Delta G / RT)$$

Convert binding energy → kinetic rates → reaction-diffusion equations

### Cellular Scale: Neurons

**Single Compartment Models:**
- LIF: Phenomenological
- Exponential IF: Better spike shape
- Adaptive Exponential IF: Adaptation
- Hodgkin-Huxley: Biophysical

**Multi-Compartment Models:**
- Divide neuron into segments
- Cable equation in each segment
- Boundary conditions at junctions
- Tools: NEURON, GENESIS

### Network Scale: Populations

**Mean-Field Models:**

Example: Wilson-Cowan (Excitatory-Inhibitory)
$$\frac{dr_E}{dt} = -r_E + f(w_{EE}r_E - w_{EI}r_I + I)$$
$$\frac{dr_I}{dt} = -r_I + f(w_{IE}r_E - w_{II}r_I + I)$$

where f(x) = 1/(1+exp(-sx)) is sigmoid activation.

**Neural Mass Models:**
- Jansen-Rit model
- Robinson model
- Generate EEG/MEG-like signals

### Systems Scale: Whole Brain

**Connectome-Based Models:**
- Structural connectivity (DTI)
- Functional connectivity (fMRI)
- Dynamics on network (neural masses at nodes)

**The Virtual Brain (TVB):**
- Large-scale brain simulation platform
- Patient-specific modeling
- Clinical applications (epilepsy, stroke)

---

## 8. Practical Implementation Guide

### Step 1: Define Your Question

- What aspect of biology are you studying?
- What level of description is appropriate?
- What predictions do you want to make?

### Step 2: Choose Model Type

**Decision Tree:**

```
Need mechanistic understanding?
├─ Yes → Biophysical model
│   ├─ Single neuron? → Hodgkin-Huxley, compartmental
│   └─ Network? → Spiking network (Brian2, NEST)
└─ No → Phenomenological model
    ├─ Spiking? → LIF, AdEx
    └─ Rate-based? → Wilson-Cowan, firing rate
```

### Step 3: Parameter Estimation

**Sources:**
- Literature values
- Experimental measurements
- Fitting to data (optimization)

**Methods:**
- Grid search
- Gradient descent
- Evolutionary algorithms
- Bayesian inference

### Step 4: Implementation

**Python Ecosystem:**

```python
# Numerical integration
from scipy.integrate import odeint, solve_ivp

# Spiking networks
import brian2  # Event-driven, equation-based
import nest    # Large-scale simulations

# Data analysis
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Dynamical systems
from scipy.optimize import fsolve  # Fixed points
from numpy.linalg import eig       # Stability
```

### Step 5: Validation

**Model Validation Checklist:**
- [ ] Does it reproduce known behaviors?
- [ ] Are parameters within biological range?
- [ ] Is it sensitive to key parameters?
- [ ] Does it make testable predictions?
- [ ] Can it generalize to new conditions?

### Step 6: Analysis

**Techniques:**
- Phase plane analysis
- Bifurcation diagrams
- Sensitivity analysis
- Information-theoretic measures

### Common Pitfalls

1. **Over-parameterization**: More parameters ≠ better model
2. **Under-validation**: Always test against independent data
3. **Ignoring scales**: Match model complexity to question
4. **Numerical instability**: Check integrator stability
5. **Biological implausibility**: Parameters must be realistic

---

## 9. Resources and References

### Essential Textbooks

**Computational Neuroscience:**
1. Gerstner et al. (2014). *Neuronal Dynamics*. Cambridge University Press.
   - Free online: https://neuronaldynamics.epfl.ch/
2. Dayan & Abbott (2001). *Theoretical Neuroscience*. MIT Press.
3. Izhikevich (2007). *Dynamical Systems in Neuroscience*. MIT Press.

**Numerical Methods:**
1. Press et al. (2007). *Numerical Recipes*. Cambridge University Press.
2. Hairer et al. (1993). *Solving Ordinary Differential Equations*. Springer.

**Nonlinear Dynamics:**
1. Strogatz (2015). *Nonlinear Dynamics and Chaos*. Westview Press.
2. Breakspear (2017). "Dynamic models of large-scale brain activity." *Nat. Neurosci.*

**Molecular Modeling:**
1. Karplus & McCammon (2002). "Molecular dynamics simulations of biomolecules." *Nat. Struct. Biol.*
2. Leach (2001). *Molecular Modelling: Principles and Applications*. Pearson.

### Software Tools

**Simulation:**
- **Brian2**: Python-based, equation-driven spiking networks
- **NEST**: Large-scale simulations (millions of neurons)
- **NEURON**: Multi-compartment models, detailed morphology
- **The Virtual Brain**: Whole-brain modeling platform

**Molecular:**
- **GROMACS**: Molecular dynamics
- **AutoDock Vina**: Molecular docking
- **PyMOL**: Visualization

**Analysis:**
- **SciPy**: Numerical integration, optimization
- **NumPy**: Array operations
- **Matplotlib**: Visualization
- **Pandas**: Data manipulation

### Key Research Papers

**Modeling:**
- Hodgkin & Huxley (1952). "A quantitative description of membrane current..." *J. Physiol.*
- Morris & Lecar (1981). "Voltage oscillations in the barnacle giant muscle fiber." *Biophys. J.*
- Wilson & Cowan (1972). "Excitatory and inhibitory interactions in localized populations..." *Biophys. J.*

**Dynamical Systems:**
- Durstewitz et al. (2023). "Reconstructing computational system dynamics from neural data..." *Nat. Rev. Neurosci.*
- Driscoll et al. (2018). "Neural dynamics: Phase space analysis." *Neuron*

**Inference:**
- El-Gazzar & van Gerven (2025). "Universal differential equations for dynamical systems..." *Front. Comput. Neurosci.*
- Brunton et al. (2016). "Discovering governing equations from data..." *PNAS*

### Online Resources

**Courses:**
- Neuromatch Academy: https://compneuro.neuromatch.io/
- Coursera: Computational Neuroscience (UW)

**Documentation:**
- Brian2: https://brian2.readthedocs.io/
- NEST: https://nest-simulator.readthedocs.io/
- SciPy: https://docs.scipy.org/

**Communities:**
- Computational Neuroscience (CNS): https://www.cnsorg.org/
- INCF: https://www.incf.org/

---

## Summary

This handout covers the essential concepts for simulation and modeling in neuroscience:

1. **Models** simplify reality to focus on essential features
2. **Differential equations** (ODEs, SDEs, PDEs) describe neural dynamics
3. **Numerical methods** (Euler, RK2, RK4) solve equations computationally
4. **Nonlinear dynamics** and phase space reveal system behavior
5. **Data-driven approaches** (RNNs, SINDy) infer dynamics from observations
6. **Multiscale modeling** connects molecules to behavior

**Key Principle**: Match model complexity to your question. Start simple, add complexity only when necessary.

**Next Steps**: Work through the Jupyter notebooks to implement these concepts hands-on!

---

*"Essentially, all models are wrong, but some are useful."* — George E. P. Box