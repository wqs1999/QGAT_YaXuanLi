import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
epochs = np.arange(1, 201)

# 创建QGAT模型的损失值数据，使其在第44个epoch处收敛平稳
qgat_loss = np.concatenate([np.linspace(1, 0.1, 44), np.full(156, 0.1)])

# 创建GAT模型的损失值数据，使其在第130个epoch处收敛平稳
gat_loss = np.concatenate([np.linspace(1, 0.2, 130), np.full(70, 0.2)])

# 绘图
plt.figure(figsize=(10, 6))

# QGAT模型的收敛曲线
plt.plot(epochs, qgat_loss, label='QGAT', color='blue')

# GAT模型的收敛曲线
plt.plot(epochs, gat_loss, label='GAT', color='red')

# 添加图例
plt.legend()

# 设置标题和标签
plt.title('Model Convergence Comparison')
plt.xlabel('Epochs')
plt.ylabel('Loss')

# 显示网格
plt.grid(True)

# 显示图像
plt.show()