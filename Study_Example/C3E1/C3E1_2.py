#matplotlib示例
import numpy as np
import matplotlib.pyplot as plt
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)
scores = [8.0, 5.0, 30]
print(softmax(scores))
# Plot softmax curves
x = np.arange(-0.5, 4.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.3 * np.ones_like(x)])
plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
#这个函数主要是用来处理多分类问题的，将��出的值转化为概率值，这样就可以用来进行多分类问题的训练了。
#matplotlib在这里的作用是用来进行绘图的，这样就可以很方便地展示softmax函数的曲线了。

