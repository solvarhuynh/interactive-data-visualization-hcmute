import matplotlib.pyplot as plt

months = ['T1', 'T2', 'T3', 'T4', 'T5']
revenue = [10, 15, 12, 50, 8]

plt.plot(months, revenue, color='green', linewidth=2)
plt.fill_between(months, revenue, color='lightgreen', alpha=0.3)

plt.title('Biểu đồ diện tích doanh thu')
plt.xlabel('Tháng')
plt.ylabel('Doanh thu (triệu VNĐ)')
plt.grid(True)
plt.show()