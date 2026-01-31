# Crank_Nicholson_Method_For_Temperature

## Heat Conduction Simulation using Crank-Nicolson Method
This repository contains a Python implementation of the Crank-Nicolson method to solve the 1D heat conduction equation using finite difference methods. The simulation models heat distribution in a rod over time, helping visualize how heat propagates under given boundary and initial conditions.

## Table of Contents
- [Introduction](#introduction)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Simulation Details](#simulation-details)  
- [Visualization](#visualization)  
- [Directory Structure](#directory-structure)  
- [License](#license)  
- [Summary](#summary)  

## Introduction
The Crank-Nicolson method is a powerful numerical technique used to solve parabolic partial differential equations, such as the heat equation. This implementation models the temperature distribution in a rod of length L = 10 meters, with boundary conditions applied at the base and tip, and a uniform initial temperature.

## System Design and Boundary Conditions

### System Overview
The simulation models heat conduction along a one-dimensional rod using the Crank-Nicolson method, a numerical technique that combines the implicit and explicit finite difference schemes. The system iteratively computes temperature values at discrete spatial points along the rod over a series of time steps, producing a stable and accurate solution to the heat equation:

\[
\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}
\]

Where:
- \(T\) is temperature (°C)  
- \(t\) is time (s)  
- \(x\) is spatial position along the rod (m)  
- \(\alpha\) is the thermal diffusivity (m²/s)  

The Crank-Nicolson method provides a second-order accurate solution in both space and time while remaining unconditionally stable for linear problems.

### Spatial and Temporal Discretization
- **Rod Length (L):** 10 meters  
- **Number of Spatial Points (Nx):** 75  
- **Number of Time Steps (Nt):** 1000  
- **Spatial Step (dx):** L / (Nx - 1)  
- **Time Step (dt):** 0.1 seconds  

The grid is uniformly spaced, and temperature values are computed at each node for every time step.

### Boundary Conditions
- **Base (x = 0):** Fixed temperature of 300°C (Dirichlet boundary condition)  
- **Tip (x = L):** Fixed temperature of 50°C (Dirichlet boundary condition)  

These Dirichlet boundary conditions ensure that the temperature at both ends of the rod remains constant throughout the simulation.

### Initial Condition
- **Uniform Initial Temperature:** 30°C along the entire rod at t = 0  

This provides a starting point for the simulation, allowing the system to evolve temperature distribution over time according to the Crank-Nicolson scheme.

### Stability Considerations
Although the Crank-Nicolson method is unconditionally stable for linear problems, the stability parameter is monitored:

\[
s = \frac{\alpha \cdot dt}{dx^2} \leq 0.5
\]

This ensures numerical accuracy and prevents oscillations in the temperature profile. Users can adjust `dx` and `dt` to refine spatial and temporal resolution while maintaining stability.

### System Workflow
1. Discretize the rod into Nx spatial points.  
2. Initialize temperature array with the uniform initial temperature.  
3. Apply boundary conditions at the base and tip.  
4. Iterate through Nt time steps using the Crank-Nicolson scheme.  
5. Solve the tridiagonal system of linear equations at each time step.  
6. Store temperature distributions in the `results/` folder for visualization.  

## Visualization

The simulation generates plots of the final temperature distribution along the rod. These visualizations illustrate how heat propagates over time using the Crank-Nicolson method.

## License

This project is licensed under the MIT License. You are free to modify and use it for educational or research purposes.

