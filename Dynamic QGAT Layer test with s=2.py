from qiskit import QuantumCircuit
import numpy as np
from qiskit_aer import Aer

# 定义一个函数来计算振幅的旋转角度
def calculate_rotation_angles(amplitudes):
    # 确保振幅已经归一化
    normalized_amplitudes = amplitudes / np.linalg.norm(amplitudes)
    num_qubits = np.log2(normalized_amplitudes.size)

    # 检查振幅长度是否是2的幂次
    assert num_qubits.is_integer(), "Amplitudes length is not a power of 2."

    num_qubits = int(num_qubits)

    # 初始化角度列表
    angles = []

    # 迭代构建角度树的每一层
    for layer in reversed(range(num_qubits)):
        num_nodes = 2 ** layer
        layer_angles = []

        # 对于每层的每个节点，计算旋转角
        for node in range(num_nodes):
            # 计算对应的振幅
            amplitude0 = normalized_amplitudes[node * 2 ** (num_qubits - layer)]
            amplitude1 = normalized_amplitudes[(node * 2 ** (num_qubits - layer)) + 2 ** (num_qubits - layer - 1)]
            # 计算角度
            angle = 2 * np.arctan2(amplitude1, amplitude0)
            layer_angles.append(angle)

        angles.append(layer_angles)

    # 展平角度列表
    flattened_angles = [angle for layer in reversed(angles) for angle in layer]
    return flattened_angles


# 定义一个均匀归一化振幅向量维度
amplitudes = np.ones(32) / np.sqrt(32)

# 计算旋转角度
rotation_angles = calculate_rotation_angles(amplitudes)

# 创建量子电路
qc = QuantumCircuit(6, 4)  # 4个经典比特，用来存储测量结果

qc.h(0)
# 应用顶层的Ry旋转
qc.ry(rotation_angles[0], 2)

# 应用中间层的受控Ry旋转
qc.cry(rotation_angles[1], 2, 3)
qc.x(2)
qc.cry(rotation_angles[2], 2, 3)
qc.x(2)

# 应用第二个节点顶层的Ry旋转
qc.ry(rotation_angles[3], 4)

# 应用中间层的受控Ry旋转
qc.cry(rotation_angles[4], 4, 5)
qc.x(4)
qc.cry(rotation_angles[5], 4, 5)
qc.x(4)

# 在q1, q2, q4应用CSWAP门，q1为控制比特
# CSWAP门的实现：CNOT和SWAP门组合
# 在q1, q2, q4应用CSWAP门，q0为控制比特
# q0 使用一控门控制 q1 -> q2
# 添加CSWAP门，q1为控制比特

qc.cry(rotation_angles[6], 0, 1)
# 在q0上使用CNOT门控制整个CSWAP门
qc.cx(0, 1)
qc.cswap(1, 2, 4)

qc.x(0)
qc.cry(rotation_angles[7], 0, 1)
qc.cswap(1, 3, 5)
qc.x(0)


# 参数化量子线路构造
qc.rx(rotation_angles[8], 1)
qc.rx(rotation_angles[9], 2)
qc.rx(rotation_angles[10], 3)

qc.cx(1, 2)
qc.cx(2, 3)
qc.cx(3, 1)

qc.ry(rotation_angles[11], 1)
qc.ry(rotation_angles[12], 2)
qc.ry(rotation_angles[13], 3)

qc.cx(1, 2)
qc.cx(2, 3)
qc.cx(3, 1)

qc.ry(rotation_angles[14], 1)
qc.ry(rotation_angles[15], 2)
qc.ry(rotation_angles[16], 3)

# 添加Z基投影测量操作
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])  # 测量q0, q1, q2, q3，并存储到经典比特[0, 1, 2, 3]中

# 打印量子电路
print(qc)