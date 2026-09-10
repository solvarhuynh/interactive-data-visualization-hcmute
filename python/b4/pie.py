import matplotlib.pyplot as plt
labels = ['Táo', 'Cam', 'Chuối', 'Xoài']
sizes = [35, 25, 20, 20]

plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%', #
    startangle=90 #
)

plt.title('Tỷ lệ các loại trái cây bán được')
plt.axis('equal')  #  
plt.show()