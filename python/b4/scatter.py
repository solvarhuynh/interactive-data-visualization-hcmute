import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 7, 4, 8, 6, 9, 8, 11, 10]

plt.scatter(x, y, color='#D81B60', marker= 'o', s=100)

plt.title('Biểu đồ Scatter Plot đơn giản')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')
plt.grid(True)

plt.show()