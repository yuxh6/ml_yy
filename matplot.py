import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("paper")
# 设置风格、尺度

import warnings
warnings.filterwarnings('ignore')
# 不发出警告

print('导入成功！')


# 1.折线图

df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))
df = df.cumsum()
df.plot(kind='line',
       style = '--.',
       alpha = 0.4,
       use_index = True,
       rot = 45,
       grid = True,
       figsize = (12,8),
       title = 'test',
       legend = True,
       subplots = False,
       colormap = 'Greens')
# subplots → 是否将各个列绘制到不同图表，默认False
# 也可以 → plt.plot(df)

# 2.散点图、气泡图

plt.figure(figsize = (12,8))
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y,marker='.',
           s = np.random.randn(1000)*100,
           cmap = 'Reds',
           c = y,
           alpha = 0.8,)
# s：散点的大小
# c：散点的颜色
# vmin,vmax：亮度设置，标量
# cmap：colormap


# 3.箱型图

df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])
df['Y'] = pd.Series(['A','B','A','B','A','B','A','B','A','B'])
print(df.head())
df.boxplot(by = 'X', figsize=(12,8))
# by：按照列分组做箱型图

# 4.小提琴图

tips = sns.load_dataset("tips")
print(tips.head())
# 加载数据

plt.figure(figsize=(12,8))
sns.violinplot(x="day", y="total_bill", data=tips,
            linewidth = 2,   # 线宽
            width = 0.8,     # 箱之间的间隔比例
            palette = 'hls', # 设置调色板
            order = ['Thur','Fri','Sat','Sun'],  # 筛选类别
            scale = 'area',  # 测度小提琴图的宽度：area-面积相同，count-按照样本数量决定宽度，width-宽度一样
            gridsize = 50,   # 设置小提琴图边线的平滑度，越高越平滑
            inner = 'box',   # 设置内部显示类型 → “box”, “quartile”, “point”, “stick”, None
           )

plt.figure(figsize=(12,8))
sns.violinplot(x="day", y="total_bill", data=tips,
               hue = 'smoker', palette="muted",
               split=True,  # 设置是否拆分小提琴图
               inner="quartile")

# 5.两个样本数据密度分布图

rs = np.random.RandomState(2)  # 设定随机数种子
df = pd.DataFrame(rs.randn(100,2),
                 columns = ['A','B'])

plt.figure(figsize=(12,8))
sns.kdeplot(df['A'],df['B'],
           cbar = True,    # 是否显示颜色图例
           shade = True,   # 是否填充
           cmap = 'Reds',  # 设置调色盘
           shade_lowest=False,  # 最外围颜色是否显示
           n_levels = 10   # 曲线个数（如果非常多，则会越平滑）
           )
# 两个维度数据生成曲线密度图，以颜色作为密度衰减显示

sns.rugplot(df['A'], color="g", axis='x',alpha = 0.5)
sns.rugplot(df['B'], color="r", axis='y',alpha = 0.5)
# 注意设置x，y轴


# 6.散点图 + 分布图

rs = np.random.RandomState(2)
df = pd.DataFrame(rs.randn(200,2),columns = ['A','B'])
# 创建数据

plt.figure(figsize=(12,8))
sns.jointplot(x=df['A'], y=df['B'],  # 设置xy轴，显示columns名称
              data=df,   # 设置数据
              color = 'k',   # 设置颜色
              s = 50, edgecolor="w",linewidth=1,  # 设置点大小、边缘线颜色及宽度(只针对scatter）
              kind = 'scatter',   # 设置类型：“scatter”、“reg”、“resid”、“kde”、“hex”
              space = 0.2,  # 设置散点图和布局图的间距
              size = 8,   # 图表大小（自动调整为正方形）
              ratio = 5,  # 散点图与布局图高度比，整型
              marginal_kws=dict(bins=15, rug=True)  # 设置柱状图箱数，是否设置rug
              )

# 7.热力图
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")

# Plot
plt.figure(figsize=(12,8), dpi= 80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)

# Decorations
plt.title('Correlogram of mtcars', fontsize=22)
plt.xticks(fontsize=12);''
plt.yticks(fontsize=12)
df.head()

