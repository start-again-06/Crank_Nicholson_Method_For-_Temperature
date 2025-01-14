import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

L = 10.0  # Length of the rod (m)
T_base = 300.0  # Boundary condition at the base (°C)
T_tip = 50.0  # Boundary condition at the tip (°C)
T_initial = 30.0  # Initial temperature (°C)
alpha = 0.01  # Thermal diffusivity (m^2/s)

Nx = 75  # Number of spatial points
Nt = 1000  # Number of time steps
dx = L / (Nx - 1)  # Spatial step size
dt = 0.1  # Time step size


s = alpha * dt / (dx**2)
if s > 0.5:
    raise ValueError("The scheme is unstable. Reduce dt or increase dx.")

T = np.ones(Nx) * T_initial
T[0] = T_base
T[-1] = T_tip

A = np.zeros((3, Nx))
A[0, 1:-1] = -s / 2
A[1, :] = 1 + s
A[2, 1:-1] = -s / 2


for n in range(Nt):
    # Right-hand side
    B = T.copy()
    B[1:-1] += s / 2 * (T[:-2] - 2 * T[1:-1] + T[2:])
    B[0] = T_base
    B[-1] = T_tip

    # Solve the system of equations
    T = solve_banded((1, 1), A, B)

x = np.linspace(0, L, Nx)
plt.plot(x, T, label=f'Nt={Nt}, dt={dt}, dx={dx}')
plt.xlabel('Position (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in the Rod (Crank-Nicolson)')
plt.legend()
plt.grid(True)
plt.show()
