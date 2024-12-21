from qiskit import QuantumCircuit
import numpy as np
from qiskit.circuit.library import RYGate

# 这里我们使用示例的均匀振幅分布来计算旋转角
# 请将这些角度替换为您具体计算得到的角度
amplitudes = np.ones(8) / np.sqrt(8)
angles = 2 * np.arcsin(amplitudes)

# 创建量子电路
qc = QuantumCircuit(3)

# 添加顶部节点的旋转
qc.ry(angles[0], 0)

# 添加中间层的旋转
qc.x(0)
qc.cry(angles[1], 0, 1)  # 零控制-Ry
qc.x(0)
qc.cry(angles[2], 0, 1)  # 正常控制-Ry

# 添加底层的旋转
qc.x(0)
qc.x(1)
ry_gate = RYGate(angles[0])
c_ry_gate = ry_gate.control(2)
qc.append(c_ry_gate, [0, 1, 2])
qc.x(1)
qc.append(c_ry_gate, [0, 1, 2])
qc.x(0)
qc.x(1)
qc.append(c_ry_gate, [0, 1, 2])
qc.x(1)
qc.append(c_ry_gate, [0, 1, 2])

# 打印量子电路图
qc.draw(output='mpl')
print(qc)
