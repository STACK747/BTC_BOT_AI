#在 Python 中，欧几里得相似度 和 余弦相似度 都是衡量 两个向量之间相似度 的方法，
# 广泛用于 数据分析、推荐系统、文本分析 等领域。在 经济学 和 金融学 中，
# 它们主要用于衡量 商品、消费者行为、股票走势、市场数据等方面的相似性。
#C3_3_3和C3_3_4主要是欧几里得相似度和余弦相似度的PY实现
#欧几里得相似度 基于欧几里得距离（Euclidean Distance），衡量两个点之间的几何距离。
#距离越小，相似度越高；距离越大，相似度越低。
import numpy as np
import matplotlib.pyplot as plt

# 生成两个数据点
A = np.array([5,5])
B = np.array([5,6])

# 计算欧几里得距离
distance = np.linalg.norm(A - B)

# 绘制点
plt.scatter(*A, color='blue', label='Point A')
plt.scatter(*B, color='red', label='Point B')

# 连接两点
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label=f'Distance: {distance:.2f}')

# 添加文本标签
plt.text(A[0], A[1], ' A', fontsize=12)
plt.text(B[0], B[1], ' B', fontsize=12)

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Euclidean Distance Visualization')
plt.legend()
plt.grid()
plt.show()
