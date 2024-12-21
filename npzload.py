import numpy as np

# 加载.npz文件
ac = np.load('D:/QGNN/Quantum-Graph-Convolutional-Network-master/Quantum-Graph-Convolutional-Network-master/data/adj.npz')

# 显示文件中包含的数组名称
print("Arrays in the .npz file:", ac.files)

# 遍历所有数组并打印它们
for array_name in ac.files:
    print(f"Array {array_name}:")
    print(ac[array_name])