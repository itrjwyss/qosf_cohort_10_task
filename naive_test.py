import matplotlib.pyplot as plt

from naive_simulation import QuantumCircuit


# Test circuit definition.
circuit = ['H', 'X', 'I', 'H', 'Z', 'CNOT', 'H', 'X', 'H', 'Z']
# Number of qubits.
qubits = 10


# List of execution times for every single test.
final_time = []
for i in range(1, qubits + 1):
    # Create a QuantumCircuit object with the specified number of qubits and circuit.
    quantum_circuit = QuantumCircuit(
        qubits=i,  # The number of qubits in the circuit
        circuit=circuit,  # A list of gates to be applied to the qubits.
    )
    # Execute the circuit and save the execution time.

    final_time.append(quantum_circuit.run_circuit())


# Plot a graphic with the execution times.
print(final_time)
plt.figure(figsize=(23, 15))
plt.plot(range(1, qubits + 1), final_time, 'o-', markersize=3)
plt.title(f"Kronecker Product Simulation of {qubits} Qubits")
plt.xlabel('qbits')
plt.ylabel('time (seconds)')
plt.grid(True)
plt.show()
