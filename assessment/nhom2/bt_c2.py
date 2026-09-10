import plotly.express as px
 
df = px.data.wind()
 
fig = px.scatter(
    df,
    x="direction",
    y="strength",
    size="frequency",          
    color="frequency",         
    hover_name="direction",
    size_max=40,
    labels={
        "frequency": "Frequency",
        "strength": "Strength",
        "direction": "Direction"
    },
    title="Wind frequency and speed chart"
)
 
# fig.write_html("bt_c2.html")
 
fig.show()