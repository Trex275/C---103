import pandas as pd
import plotly.express as ex

df =pd.read_csv("data.csv")

fig = ex.scatter(df, x = "Country", y = "Per capita", color = "Country", size = "Percentage")
fig.show()