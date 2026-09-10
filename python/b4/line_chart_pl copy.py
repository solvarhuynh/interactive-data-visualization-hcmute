import plotly.express as px

months = ['T1', 'T2', 'T3', 'T4', 'T5']
revenue = [10, 15, 12, 22, 18]

fig = px.line(
    x=months,
    y=revenue,
    markers=True,
    title='Doanh thu theo tháng (Interactive Line Chart)',
    labels={'x': 'Tháng', 'y': 'Doanh thu (triệu VNĐ)'}
)
fig.show()