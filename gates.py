import numpy as np


# Initial Quantum States
ket_0 = [1, 0]
ket_1 = [0, 1]


# Imaginary Unit
i = 1j


# Identity Gate
gate_i = np.array([
    [1, 0],
    [0, 1]
])


# Pauli's Gates
gate_x = np.array([
    [0, 1],
    [1, 0]
])
gate_y = np.array([
    [0, -i],
    [i, 0]
])
gate_z = np.array([
    [1, 0],
    [0, -1]
])


# Hadamard Gate
alpha_h = 1/np.sqrt(2)
gate_h = np.array([
    [alpha_h, alpha_h],
    [alpha_h, -alpha_h]
])


# CNOT Gate
gate_c_not = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])
