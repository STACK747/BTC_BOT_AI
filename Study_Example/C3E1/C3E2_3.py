import numpy as np
import pandas as pd
import os
# 生成随机数据
num_rows = 100000  # 数据量级 10 万行
num_cols = 5       # 生成 5 列数据

data = np.random.randint(0, 1000, size=(num_rows, num_cols))  # 生成 0-1000 之间的随机整数

# 创建 DataFrame
df = pd.DataFrame(data, columns=[f'Column_{i+1}' for i in range(num_cols)])
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "random_data.csv")  # 获取桌面路径
df.to_csv(desktop_path, index=False)
# 保存到 CSV 文件

print(f"CSV 文件已保存至：{desktop_path}")
print(df.head())
print(df.shape)
