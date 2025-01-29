# Crank_Nicholson_Method_For_Temperature

🔥 Heat Conduction Simulation using Crank-Nicolson Method

This repository contains a Python implementation of the Crank-Nicolson method to solve the 1D heat conduction equation using finite difference methods. The simulation models heat distribution in a rod over time.

📌 Table of Contents

📖 Introduction

🛠 Requirements

📥 Installation

🚀 Usage

📊 Simulation Details

📈 Visualization

📂 Directory Structure

📜 License

📖 Introduction

The Crank-Nicolson method is a powerful numerical technique used to solve parabolic partial differential equations, such as the heat equation. This implementation models the temperature distribution in a rod of length L = 10 meters, given boundary conditions at the base and tip.

🛠 Requirements

Make sure you have the following dependencies installed:

pip install numpy matplotlib scipy

📥 Installation

Clone this repository and navigate to the project directory:

git clone https://github.com/your-username/heat-conduction-solver.git
cd heat-conduction-solver

🚀 Usage

Run the script to simulate heat conduction and visualize the temperature distribution:

python heat_conduction.py

📊 Simulation Details

Rod Length: 10.0 meters

Thermal Diffusivity: 0.01 m²/s

Boundary Conditions:

Base temperature: 300°C

Tip temperature: 50°C

Initial Condition: Uniform 30°C throughout the rod

Grid:

Nx = 75 spatial points

Nt = 1000 time steps

dx = L / (Nx - 1)

dt = 0.1 seconds

Stability Check: Ensures the numerical scheme remains stable (s ≤ 0.5)

📈 Visualization

The simulation plots the final temperature distribution in the rod. The results help understand how heat propagates over time using the Crank-Nicolson method.

📂 Directory Structure

├── heat_conduction.py       # Main script for heat simulation
├── requirements.txt         # Required dependencies
├── README.md                # Project documentation
└── results/                 # Folder for generated plots

📜 License

This project is licensed under the MIT License. Feel free to modify and use it for your work.
