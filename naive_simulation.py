import numpy as np
import time

from gates import gate_i, ket_0
from gates import gate_x, gate_y, gate_z
from gates import gate_h
from gates import gate_c_not


def operate_gate(gate, state):
    """
        Applies a gate to a given quantum state.

        Args:
            gate: The gate matrix to apply.
            state: The quantum state vector

        Returns:
            The updated quantum state vector after applying the gate.
    """
    return np.kron(gate, state)


def run_circuit(state, circuit):
    """
        Applies a circuit (list of gates) to a quantum state.

        Args:
            state: The quantum state vector.
            circuit: A list of gates to be applied to the qubit state.

        Returns:
            The updated quantum state vector after applying the circuit.
    """
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


class QuantumCircuit:
    """
        Representation of a quantum circuit.

        Args:
            qubits: The number of qubits in the circuit.
            circuit: A list of gates to be applied to the qubits.

        Attributes:
            qubits: The number of qubits.
            state_vector: The initial state vector of the qubits.
            circuits: A list of gates to be applied to the qubits.

        Methods:
            run_circuit():
                Simulates the quantum circuit by applying the gates sequentially to the state vector using kronecker product (kron).
                Measures the execution time of the simulation.
                Returns the execution time.
    """

    def __init__(self, qubits, circuit):
        """
            Initializes a QuantumCircuit object.

            Args:
                qubits: The number of qubits in the circuit.
                circuit: A list of gates to be applied to the qubits.

            Assert
                qubits: Up or equals to 1.
                circuit: Cannot be empty.
        """
        self.qubits = qubits
        n_tuples = (2 ** qubits) // 2
        self.state_vector = np.array(ket_0 * n_tuples)
        self.circuits = np.array(circuit)

        assert self.state_vector.size != 0 and self.circuits.size != 0


    def run_circuit(self):
        """
            Simulates the quantum circuit using tensor contractions.

            Args:
                No args

            Returns:
                The execution time of the simulation.

            Simulates the quantum circuit by applying the gates sequentially to the state vector using tensor contractions.
            Measures the execution time of the simulation.
            Returns the execution time.
        """
        start = time.time()
        run_circuit(self.state_vector, self.circuits)
        end = time.time()
        return end - start
