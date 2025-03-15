#人生苦短，我用PYTHON!
#numpy例子
#这个例子是用来展示如何使用numpy库来进行softmax函数的计算。
#NumPy（Numerical Python）是 Python 中最常用的 科学计算库，提供 高效的多维数组（ndarray） 和 数学计算函数。它可以加速 矩阵运算、线性代数、傅立叶变换、随机数生成 等操作，是 机器学习、数据分析、图像处理 等领域的基础工具。
#加速计算
import numpy as np
import matplotlib.pyplot as plt
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)
scores = [3.0, 1.0, 0.2]
print(softmax(scores))
# Plot softmax curves
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
#这个函数主要是用来处理多分类问题的，将��出的值转化为概率值，这样就可以用来进行多分类问题的训练了。
#比如我们有一个输出层的值为[3.0, 1.0, 0.2]，我们可以使用softmax函数将其转化为概率值，选择概率值最大的那个作为输出的类别。
#softmax函数的公式为：softmax(x) = exp(x) / sum(exp(x))，其中exp(x)表示e的x次方，sum(exp(x))表示对exp(x)求和。
#这个函数的特点是对于输入的值，输出的值是0到1之间的概率值，并且输出的概率值之和为1。
#这个函数的缺点是对于输入的值的大小比较敏感，如果输入的值比较大，那么输出的概率值就会很小，反之亦然。
#这个函数的优点是可以将输出的值转化为概率值，这样就可以用来进行多分类问题的训练了。
#numpy在这个里面的作用是用来进行矩阵运算的，这样就可以很方便的进行softmax函数的计算了。


