import numpy as np
import matplotlib.pyplot as plt

# 定义两个向量
A = np.array([2, 10])
B = np.array([4, 6])

# 计算余弦相似度
cosine_sim = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

# 绘制坐标轴
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid()

# 绘制向量
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector A')
plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector B')

# 添加文本标签
plt.text(A[0], A[1], ' A', fontsize=12)
plt.text(B[0], B[1], ' B', fontsize=12)

plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title(f'Cosine Similarity: {cosine_sim:.2f}')
plt.legend()
plt.show()
