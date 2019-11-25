import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Seasons_Stats.csv")

# drop the player Eddie Johnson , Because he appears twice

df = df[df.Player != 'Eddie Johnson']

# add new column - that sum the player points till that period od time

df['Total_PTS'] = df.groupby('Player')['PTS'].cumsum()

# Minimize the columns to see clearly the columns that necessary

df_new = df[['Player','Year','PTS','Age','Total_PTS']]

# find who are the top 20 points scoring

top20players = df_new.groupby(['Player']).sum().sort_values('PTS',ascending=False).head(20)

# turn the table into list with the name of the players

name_20_lst = list(top20players.index)

# filter the player column to the 20 top scoring

table_20 = df_new[df_new.Player.isin(name_20_lst)]

# drop the double index column

table_20.reset_index(drop=True , inplace = True)
print(table_20)



