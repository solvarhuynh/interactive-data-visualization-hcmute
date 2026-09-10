import matplotlib.pyplot as plt

categories = ['Táo', 'Cam', 'Xoài', 'Chuối']
quantities = [20, 35, 15, 25]
colors = ['red', 'orange', 'green', 'yellow']

plt.bar(categories, quantities, color=colors)

plt.title('Số lượng trái cây bán được')
plt.xlabel('Loại trái cây')
plt.ylabel('Số lượng (kg)')

plt.show()