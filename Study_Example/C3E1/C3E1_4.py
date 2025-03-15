#随机数据处理
#对random_data.csv中的Column_1和Column_2的前500行进行绘图，图表最大值为10000。
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
#Study_Example/C3E1/random_data.csv
df = pd.read_csv('random_data.csv')
df['Column_1'][:500].plot()
df['Column_2'][:500].plot()
plt.ylim(0, 2000)
plt.show()








