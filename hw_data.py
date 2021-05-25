import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px
df = pd.read_csv("data.csv")
student_df = df.loc[df['student_id']=="TRL_xsl"]
print(student_df.groupby("level")["attempt"].mean())
fig = px.scatter(df,x = "student_id",y = "level",color = "attempt")
fig.show()