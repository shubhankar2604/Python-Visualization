import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#to check, run the command at pw labs in jupyter notebook

x = np.arange(1,11)
y = 2 * x
y2 = 3 * x


# 1) LINE PLOT

plt.plot(x,y)
plt.title("Basic Line Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()

#we can also customize the lines...
plt.plot(x,y, color="g", linestyle = ":", linewidth = 2)
plt.show()

#plotting multiple lines
plt.plot(x,y, color = "red", linestyle = "--")
plt.plot(x,y2, color = "green", linestyle = "-.")
plt.title("Double Line Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()


#plotting subplots (rows, columns, index)
plt.subplot(1,2,1)
plt.plot(x,y, color = "red", linestyle = ":")

plt.subplot(1,2,2)
plt.plot(x,y2, color = "green", linestyle = "-.")

plt.show()



# 2) BAR PLOT

student = {"Bob":87,"Matt":56,"Sam":27}
names = list(student.keys())
values = list(student.values())

plt.bar(names,values)
plt.title("Bar Plot")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.grid(True)          #to show grid.. optional
plt.show()


#horizontal plot
plt.barh(names,values,color='g')
plt.title("Bar Plot")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.grid(True)
plt.show()



# 3) SCATTER PLOT

p = [2,4,6,7,11]
q = [4,1,8,3,7]
r = [3,6,9,12,5]

plt.scatter(p,q)
plt.title("Scatter Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()


# creative scatter plot
colours = np.random.randint(50)
sizes = 1000 * np.random.rand(50)
plt.scatter(p,q, c = colours, s = sizes, alpha = .5)     # alpha stands for intensity
plt.title("Scatter Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()




#plotting two scatter plots in one graph
# using markers
# 's' stands for size of the marker

plt.scatter(p,q,marker="*",c="g",s=100)
plt.scatter(p,r,marker=".",c="r",s=200)
plt.title("Scatter Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()



# subplots in scatter plot

p = [2,4,6,7,11]
q = [4,1,8,3,7]
r = [3,6,9,12,5]

plt.subplot(1,2,1)
plt.scatter(p,q,marker="*",c=['g','r','orange','blue', 'yellow'],s=100)

plt.subplot(1,2,2)
plt.scatter(p,r,marker=".",c="r",s=200)
plt.show()


# 3d projections in scatter plot

sb = np.random.rand(50)
ab = np.random.rand(50)
mb = np.random.rand(50)

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.scatter(sb,ab,mb)
plt.show()




# 4) HISTOGRAM

data = [1,2,3,3,2,5,4,6,3,4,7,8,8,9,2]
# histogram shows the mode in the list, i.e. no. of repetations of a data.. eg. according to 2 repeats 3 limes, 3 repeates 3 times.. etc

plt.hist(data)
plt.show()


#histogram from a dataframe

iris = pd.read_csv('iris.csv')
iris.head()

plt.hist(iris['Sepal.Length'], bins = 30, color = 'green')  # bins is the no. of towers in the histogram
plt.show()



# 5) BOXPLOT

one = [2,3,5,4,7,6]
two = [4,5,11,6,8,3]
three = [2,5,4,8,5,1]

info = list([one,two,three])
plt.boxplot(info)
plt.show()


# 5) VIOLINPLOT

plt.violinplot(data, showmedians=True)  #showmedians is used to show the medians in the plot
plt.show()


# three plots in one
plt.violinplot(info)
plt.show()


# 6) PIE PLOT

fruit = ['Apple','Mango','Pear','Guava']
quantity = [45,56,32,71]

plt.pie(quantity, labels = fruit)
plt.show()


# also, change the colors and add percentage to the plot,, autopct
# here 0.2f indicates that the percentage would be upto 2 decimal places
plt.pie(quantity, labels = fruit, colors=['yellow','blue','red','green'], autopct = '%0.2f%%')
plt.show()


# 7) DOUGHNUT PLOT

# radius denotes the size of the plot
# now, adding a white/black pie plot in between the main pie plot would seem like a doughnut plot
plt.pie(quantity, labels = fruit, radius = 1.5)
plt.pie([1], colors = "white", radius = 0.85)      # a simple list with one element
plt.show()