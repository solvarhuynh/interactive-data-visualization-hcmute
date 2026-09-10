import plotly.graph_objects as go

months = ['T1', 'T2', 'T3', 'T4', 'T5']
rev_2023 = [10, 15, 12, 22, 18]
rev_2024 = [14, 18, 16, 28, 24]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=months,
    y=rev_2024,
    mode='lines+markers',
    name='Năm 2024',
    line=dict(color='#FFA500'),
    fill='tozeroy',                      
    fillcolor='rgba(255, 165, 0, 0.25)' 
))

fig.add_trace(go.Scatter(
    x=months,
    y=rev_2023,
    mode='lines+markers',
    name='Năm 2023',
    line=dict(color='#0000FF')
))

fig.update_layout(
    title='So sánh doanh thu 2023 vs 2024',
    xaxis_title='Tháng',
    yaxis_title='Doanh thu (triệu VNĐ)',
    hovermode='x unified'
)

fig.show()