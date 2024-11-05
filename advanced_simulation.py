import numpy as np
import time

from gates import gate_i, ket_0
from gates import gate_x, gate_y, gate_z
from gates import gate_h
from gates import gate_c_not


def operate_single_gate(gate, state, n_qubits):
    """
        Applies a gate to a given quantum state.

        Args:
            gate: The gate matrix to apply.
            state: The quantum state vector.
            n_qubits: The number of qubits in the state.

        Returns:
            The updated quantum state vector after applying the gate.
    """
    state_reshaped = state.reshape(tuple([2] * n_qubits))

    state_reshaped = np.tensordot(
        np.eye(2),
        np.tensordot(gate, state_reshaped, axes=1),
        axes=1
    )

    state = state_reshaped.reshape(2 ** n_qubits)
    return state


def run_circuit(state, circuit, n_qubits):
    """
        Applies a circuit (list of gates) to a quantum state.

        Args:
            state: The quantum state vector.
            circuit: A list of gates to be applied to the qubit state.
            n_qubits: The number of qubits in the state.

        Returns:
            The updated quantum state vector after applying the circuit.
    """
    for gate in circuit:
        match gate:
            case 'I':  # Identity Gate
                state = operate_single_gate(gate_i, state, n_qubits)

            case 'X':  # Pauli's X Gate
                state = operate_single_gate(gate_x, state, n_qubits)
            case 'Y':  # Pauli's Y Gate
                state = operate_single_gate(gate_y, state, n_qubits)
            case 'Z':  # Pauli's Z Gate
                state = operate_single_gate(gate_z, state, n_qubits)

            case 'H':  # Hadamard Gate
                state = operate_single_gate(gate_h, state, n_qubits)

            case 'CNOT':  # CNOT Gate
                state = operate_single_gate(gate_c_not, state, n_qubits)

            case _:
                print("Unknown gate")

    return state


class QuantumCircuit:
    """
        Representation of a quantum circuit.

        Args:
            n_qubits: The number of qubits in the circuit.
            circuit: A list of gates to be applied to the qubits.

        Attributes:
            qubits: The number of qubits.
            state_vector: The initial state vector of the qubits.
            circuits: A list of gates to be applied to the qubits.

        Methods:
            run_circuit():
                Simulates the quantum circuit by applying the gates sequentially to the state vector using tensor contractions.
                Measures the execution time of the simulation.
                Returns the execution time.
    """

    def __init__(self, n_qubits, circuit):
        """
            Initializes a QuantumCircuit object.

            Args:
                n_qubits: The number of qubits in the circuit.
                circuit: A list of gates to be applied to the qubits.

            Assert
                n_qubits: Up or equals to 1.
                circuit: Cannot be empty.
        """
        self.qubits = n_qubits
        n_tuples = (2 ** n_qubits) // 2
        self.state_vector = np.array(ket_0 * n_tuples).reshape(tuple([2] * n_qubits))
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
        run_circuit(self.state_vector, self.circuits, self.qubits)
        end = time.time()
        return end - start
