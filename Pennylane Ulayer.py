import pennylane as qml
from pennylane import numpy as np


def create_U_circuit(params):
    n_qubits = 2
    dev = qml.device('default.qubit', wires=n_qubits)

    @qml.qnode(dev)
    def circuit(params):
        # 对每个量子比特应用小u（RZ，RY，RZ）
        for i in range(n_qubits):
            qml.RZ(params[i][0], wires=i)
            qml.RY(params[i][1], wires=i)
            qml.RZ(params[i][2], wires=i)

        # 应用受控CNOT门
        qml.CNOT(wires=[1, 0])

        # 第一个量子比特应用RZ门
        qml.RZ(params[2][0], wires=0)

        # 第二个量子比特应用RY门
        qml.RY(params[2][1], wires=1)

        # 应用受控CNOT门
        qml.CNOT(wires=[0, 1])

        # 第二个量子比特应用RY门
        qml.RY(params[2][2], wires=1)

        # 应用受控CNOT门
        qml.CNOT(wires=[1, 0])

        # 对每个量子比特应用小u（RZ，RY，RZ）
        for i in range(n_qubits):
            qml.RZ(params[i + 3][0], wires=i)
            qml.RY(params[i + 3][1], wires=i)
            qml.RZ(params[i + 3][2], wires=i)

        return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

    return circuit


# 示例参数
params = np.random.rand(6, 3)  # 为每个小u设置6组参数

circuit = create_U_circuit(params)
result = circuit(params)
print(result)