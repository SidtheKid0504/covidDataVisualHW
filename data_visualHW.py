import pandas as pd
import plotly_express as pl

csv_data = pd.read_csv('./hwFiles/data/covid_data.csv')

fig = pl.scatter(csv_data, x= "date", y="cases", color="country", title="Covid Cases In Countries")

fig.show()