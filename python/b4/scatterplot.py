import plotly.express as px
import pandas as pd

# Dữ liệu ví dụ
df = pd.DataFrame({
    'Giờ học': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Điểm thi': [45, 52, 58, 60, 68, 75, 82, 88, 95],
    'Tỷ lệ chuyên cần (%)': [60, 65, 70, 75, 80, 85, 90, 95, 100],
    'Khối ngành': ['Tự nhiên', 'Xã hội', 'Tự nhiên', 'Xã hội', 'Tự nhiên',
                   'Xã hội', 'Tự nhiên', 'Xã hội', 'Tự nhiên']
})

fig = px.scatter(
    df,
    x='Giờ học',
    y='Điểm thi',
    color='Khối ngành',              # Phân màu điểm theo nhóm
    size='Tỷ lệ chuyên cần (%)',      # Bubble chart
    hover_data=['Tỷ lệ chuyên cần (%)'], # Thông tin hiện thêm khi rê chuột
    title='Mối liên hệ giữa Giờ học và Điểm thi',
    size_max=20                      # Kích thước bong bóng tối đa
)

fig.show()