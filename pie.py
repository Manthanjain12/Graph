import matplotlib.pyplot as plt
import numpy as np 
labels = ['a', 'b', 'c', 'd']
values = [15,30,45,60]
plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.title("Data visualization(pie chart)")
plt.show()
data_points = [10,20,30,40,50]
freq = [3,7,12,8,5]
cum_freq = np.cumsum(freq)
plt.plot(data_points,cum_freq,marker='o',color='yellow}')
plt.title("Less than ogive")
plt.xlabel("Class boundaries")
plt.ylabel("cumulative frequency")
plt.grid()
plt.show()
