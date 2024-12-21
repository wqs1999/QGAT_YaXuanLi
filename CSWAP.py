import pennylane as qml
from pennylane.operation import Operation
import numpy as np


# 定义受控交换门
class CSWAP(Operation):
    num_wires = 3
    num_params = 0
    grad_method = None

    @staticmethod
    def decomposition(wires):
        control, target1, target2 = wires
        return [
            qml.CNOT(wires=[target2, target1]),
            qml.Toffoli(wires=[control, target1, target2]),
            qml.CNOT(wires=[target2, target1])
        ]

    @staticmethod
    def matrix():
        return np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
        ])

    def __init__(self, wires):
        super().__init__(wires=wires)


# 定义量子设备
dev = qml.device("default.qubit", wires=3)


@qml.qnode(dev)
def circuit():
    # 初始化量子比特
    qml.Hadamard(wires=0)  # 将第一个量子比特置于叠加态
    qml.PauliX(wires=1)  # 将第二个量子比特置于 |1> 态

    # 使用自定义的受控交换门
    CSWAP(wires=[0, 1, 2])

    # 测量
    return qml.state()


# 运行电路
state = circuit()
print(state)

# 打印电路
drawer = qml.draw(circuit)
print(drawer())
