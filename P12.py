import pandas as pd
import plotly.express as pe
import plotly.figure_factory as pff

data=pd.read_csv("SM.csv")
fig=pff.create_distplot([data["Marks In Percentage"].tolist()],["Marks"])
fig.show()