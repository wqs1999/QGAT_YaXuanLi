import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 输入每个噪声水平下的20个测试准确率数据
test_accuracies = {
    0: [59.68, 60.35, 59.78, 59.95, 59.76, 59.64, 59.70, 59.93, 60.08, 60.19, 59.99, 60.15, 59.78, 60.36, 60.02, 60.18, 60.19, 59.88, 60.19, 59.63],
    0.001: [59.27, 59.53, 59.13, 59.49, 59.44, 59.70, 59.38, 59.86, 59.74, 59.75, 59.37, 59.54, 59.60, 59.71, 59.73, 59.89, 59.51, 59.69, 59.60, 59.24],
    0.01: [59.15, 58.98, 59.53, 59.04, 59.63, 58.81, 58.34, 59.16, 59.85, 59.34, 58.46, 59.37, 58.88, 58.41, 58.35, 59.47, 58.43, 58.22, 59.81, 59.05],
    0.1: [57.62, 56.95, 56.64, 56.41, 57.71, 56.47, 56.81, 57.45, 57.44, 56.35, 56.33, 56.63, 57.42, 57.05, 59.36, 56.14, 57.51, 56.70, 56.16, 56.93]
}

# 准备数据用于绘图
data = []
for noise_level, accuracies in test_accuracies.items():
    for accuracy in accuracies:
        data.append([noise_level, accuracy])

# 转换为NumPy数组
data = np.array(data)

# 创建箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(x=data[:, 0], y=data[:, 1], width=0.5)

# 添加图像标题和标签
plt.title('')
plt.xlabel('Noise Parameter')
plt.ylabel('Test Accuracy')

# 显示图像
plt.show()

