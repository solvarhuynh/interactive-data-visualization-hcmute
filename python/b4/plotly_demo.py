import plotly.express as px

categories = ['Táo', 'Cam', 'Xoài', 'Chuối', 'Nho']
quantities = [20, 35, 15, 25, 30]

fig = px.bar(
    x=categories,
    y=quantities,
    labels={'x': 'Loại trái cây', 'y': 'Số lượng (kg)'},
    title='Số lượng trái cây bán được (Có tương tác)',
    color=categories, 
    text_auto=True)
fig.update_layout(xaxis={'categoryorder': 'total descending'})

fig.show()

fig.write_html("python/b4/bieu_do_tuong_tac.html")