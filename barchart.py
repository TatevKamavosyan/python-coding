import matplotlib.pyplot as plt


categories=['A','B','C','D','E']
values=[10,12,5,8,3]

plt.bar(categories,values)
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show