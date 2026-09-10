import plotly.express as px

months = ['T1', 'T2', 'T3', 'T4', 'T5']
rev_2023 = [10, 15, 12, 22, 18]
rev_2024 = [14, 18, 16, 28, 24]

fig = px.area(
    x=months,
    y=rev_2024,
    markers=True,
    title='So sánh doanh thu 2023 vs 2024',
    labels={'x': 'Tháng', 'y': 'Doanh thu (triệu VNĐ)'}
)

fig.data[0].name = 'Năm 2024'
fig.data[0].showlegend = True
fig.update_traces(
    line_color='#FFA500',
    fillcolor='rgba(255, 165, 0, 0.25)'
)

fig_line = px.line(
    x=months,
    y=rev_2023,
    markers=True
)
fig_line.data[0].name = 'Năm 2023'
fig_line.data[0].showlegend = True
fig_line.update_traces(line_color='#0000FF')

fig.add_trace(fig_line.data[0])

fig.update_layout(hovermode='x unified')

fig.show()