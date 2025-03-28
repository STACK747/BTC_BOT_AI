#四分位是统计学中的一个概念，是指在统计学中把所有数值由小到大排列并分成四等份，处于三个分割点位置的数值就是四分位数。
#这三个分割点位置分别是：第一四分位数（Q1），第二四分位数（Q2），第三四分位数（Q3）。
#第一四分位数（Q1）又称“较小四分位数”，第二四分位数（Q2）又称“中位数”，第三四分位数（Q3）又称“较大四分位数”。
#分别是数据从小到的排列后的25%，50%，75%的位置上的数值。
#四分位距是第三四分位数与第一四分位数的差值，即Q3-Q1。
#四分位差是一组数据的上四分位数与下四分位数之差，即Q3-Q1。
#图形识别：箱线图：从下到上依次是下边缘，Q1,中位数，Q3,上边缘，异常值。
#箱线图绘制
import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(2, 10, 500)
#np.random.normal的参数分别是loc（均值），scale（标准差），size（输出的shape）
plt.boxplot(data, patch_artist=True, showmeans=True)
plt.show()


