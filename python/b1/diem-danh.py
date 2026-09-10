import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60
)
fig.write_html("python/diem-danh-py/b1.html")
fig.show()

