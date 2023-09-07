import seaborn as sns
import numpy as np

x = np.arange(1,11)
y1 = 2 * x
y2 = 3 * x

iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')

# 1) SCATTER PLOT

sns.scatterplot(x = x, y = y1)
sns.scatterplot(x = iris.sepal_length, y = iris.sepal_width)


# 2) HISTOGRAM

sns.histplot(x)

# 3) DISTANCE PLOT (same as histogram)

sns.displot(x)


# 4) JOIN PLOT (scatter + histogram)

sns.jointplot(x = iris.sepal_length, y = iris.sepal_width)


# 5) PAIR PLOT (all dimensions of graphs)

sns.pairplot(tips)



# use 'hue' for visualizing a certain data differently from the dataset by color
# use 'style' for visualizing a certain data differently from the dataset by shapes / symbols
sns.relplot(x= tips.total_bill, y= tips.tip, data=tips, hue = 'smoker', style= 'size')



## SEABORN also has other basic plots like, Barplot, Histogram, Violinplot, Jointplot, etc.