# Subtask 1: Naive simulation using matrix multiplication

## Simulation implementation

[naive_simulation.py](naive_simulation.py) is the file with the implementation to simulate the execution of the quantum circuit.

### Used libraries

- **Numpy**: for handling vectors and operations on them.
- **time**: to calculate the simulation run time.

### Functions and objects

```python
def operate_gate(gate, state):
    return np.kron(gate, state)
```

`operate_gate` is a function to use the Kronecker Product for apply a quantum gate to a quantum state, is implemented using the `np.kron`
function.

```python
def run_circuit(state, circuit):
    for gate in circuit:
        match gate:
            case 'I':  # Identity Gate
                state = operate_gate(gate_i, state)

            case 'X':  # Pauli's X Gate
                state = operate_gate(gate_x, state)
            case 'Y':  # Pauli's Y Gate
                state = operate_gate(gate_y, state)
            case 'Z':  # Pauli's Z Gate
                state = operate_gate(gate_z, state)

            case 'H':  # Hadamard Gate
                state = operate_gate(gate_h, state)

            case 'CNOT':  # CNOT Gate
                state = operate_gate(gate_c_not, state)

            case _:
                print("Unknown gate")

    return state
```

`run_circuit (General)` is a function to apply sequentially all the gates in the circuit list to a quantum state. 
The logic is to check every gate on the list, verify which gate is and apply it 
(if is a gate defined as admitted) using the function described previously `operate_gate`

```python
class QuantumCircuit
```

`QuantumCircuit` is the definition of a Quantum Circuit with a state vector, a circuit to apply and the number of qubits represented at the state vector.

```python
def __init__(self, qubits, circuit):
    self.qubits = qubits
    n_tuples = (2 ** qubits) // 2
    self.state_vector = np.array(ket_0 * n_tuples)
    self.circuits = np.array(circuit)

    assert self.state_vector.size != 0 and self.circuits.size != 0
```

This is the `QuantumCircuit` constructor, will receive the number of `qubits` to handle and the `circuit` to apply.
The state vector is initialized with quantum state |0⟩, this applies to all the qubits.

```python
def run_circuit(self):
    start = time.time()
    run_circuit(self.state_vector, self.circuits)
    end = time.time()
    return end - start
```

`run_circuit (QuantumCircuit)` class function, takes the simulation run time and returns the final time. 
To execute the circuit, uses the general function `run_circuit (General)` that was already described.


