import plotly.express as px

df = px.data.tips()

fig = px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="time",      
    size="size",        
    hover_data=["sex"],
    title="Tổng hóa đơn vs Tiền Tip"
)
fig.write_html("python/b1/phan1-py.html")
fig.show()
