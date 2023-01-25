import pandas as pd

import plotly.express as px
import plotly.graph_objects as go


accidents_par_jour = pd.read_csv("../data/Data_plotly/accidents_par_jour.csv")
df_date_grav = pd.read_csv("../data/Data_plotly/df_date_grave.csv", sep=",")
grav_par_jour = pd.read_csv("../data/Data_plotly/grav_par_jour.csv", sep=",")


figplotly_1 = px.line(
    accidents_par_jour,
    x="date",
    y="nombre",
    labels={"date": "Dates", "nombre": "Nombre d'accidents"},
    title="Évolution du nombre d'accidents par jour de 2005 à 2020",
)
figplotly_1.update_traces(line_color="green", line_width=0.5)

figplotly_2 = px.line(
    df_date_grav,
    x="date",
    y=["0", "1"],
    labels={"date": "Dates", "value": "Nombre d'accidents"},
    title="Évolution du nombre d'accidents en fonction de leur gravité par jour de 2005 à 2020",
)
figplotly_2.update_traces(line_width=0.5)
newnames = {"0": "accidents légers", "1": "accidents graves"}
figplotly_2.for_each_trace(lambda trace: trace.update(name = newnames[trace.name]))


figplotly_3 = px.line(
    grav_par_jour,
    x="date",
    y="accident_grave",
    labels={"date": "Dates", "accident_grave": "Gravité moyenne"},
    title="Évolution de la gravité moyenne des accidents par jour de 2005 à 2020",
)
figplotly_3.update_traces(line_color="orange", line_width=0.5)
""" newname = {"accident_grave": "gravité"}
figplotly_3.for_each_trace(lambda trace: trace.update(name = newname[trace.name])) """
