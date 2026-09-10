import plotly.express as px

months = ['T1', 'T2', 'T3', 'T4', 'T5']
revenue = [10, 15, 12, 22, 18]

# fig = px.line(
#     x=months,
#     y=revenue,
#     markers=True,
#     title='Doanh thu theo tháng (Interactive Line Chart)',
#     labels={'x': 'Tháng', 'y': 'Doanh thu (triệu VNĐ)'}
# )

fig = px.area(
    x=months,
    y=revenue,
    title='Biểu đồ diện tích doanh thu (Interactive Area Chart)',
    labels={'x': 'Tháng', 'y': 'Doanh thu (triệu VNĐ)'},
    markers=True
)

fig.update_traces(
    line_color='red',
    fillcolor='rgba(255, 0, 0, 0.3)'
)

fig.show()