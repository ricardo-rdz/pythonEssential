import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('fifa_players.csv')

#print(df.head())
#print(df.info())
#print(df["age"].max())
#print(df.loc[df["age"] == df["age"].max()])
#print(df["age"].value_counts())
#print(df["nationality"].value_counts())
conteo = df["age"].value_counts()
conteo.plot(kind="bar")
plt.title("edades de los jugadores")
plt.xlabel("edad")
plt.ylabel("cantidad de jugadores")
plt.show()