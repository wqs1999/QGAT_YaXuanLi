import numpy as np

# 指定要读取的 .npy 文件路径
file_path = "D:/QGNN/Quantum-Graph-Convolutional-Network-master/Quantum-Graph-Convolutional-Network-master/data/middle_layer.npy"

# 使用 NumPy 的 load 函数读取 .npy 文件
data = np.load(file_path)

# 打印读取的数据
print("Loaded data:")
print(data)