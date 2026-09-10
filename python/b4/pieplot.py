import plotly.express as px

labels = ['Táo', 'Cam', 'Chuối', 'Xoài']
sizes = [35, 25, 20, 20]

fig = px.pie(
    names=labels,
    values=sizes,
    title='Tỷ lệ trái cây bán được (Interactive Pie Chart)',
    hole = 0.4  # đục lỗ
)

fig.update_traces( #
    textinfo = 'percent+label',
    textposition = 'inside',
    pull=[0,0.115,0,0]
)
fig.show()