import matplotlib.pyplot as plt

x = ['Q1', 'Q2', 'Q3', 'Q4']
y = [10000, 12000, 11000, 8000]
plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.title('Sales by quarter')
#creates bar chart
#plt.bar(x, y)

#creates a line chart and makes it a double dashed line
plt.plot(x, y, marker = 'o', color = 'yellow', linestyle = '--')
plt.show()
