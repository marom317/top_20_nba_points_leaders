
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

df = pd.read_csv("Seasons_Stats.csv")

# drop the player Eddie Johnson , Because he appears twice

df = df[df.Player != 'Eddie Johnson']

# add new column - that sum the player points till that period od time

df['Total_PTS'] = df.groupby('Player')['PTS'].cumsum()

# Minimize the columns to see clearly the columns that necessary

df_new = df[['Player','Year','PTS','Age','Total_PTS']]

# find who are the top 20 points scoring

top20players = df_new.groupby(['Player']).sum().sort_values('PTS',ascending=False).head(20)
# reverse the list
top20players = top20players.sort_values('PTS', ascending=True)
# turn the table into list with the name of the players

name_20_lst = list(top20players.index)

top_20_PTS =list(top20players.PTS)

top_20_str = [str(item) for item in top_20_PTS]
# filter the player column to the 20 top scoring

table_20 = df_new[df_new.Player.isin(name_20_lst)]

# drop the double index column

table_20.reset_index(drop=True , inplace = True)
colors = dict(zip([
    'Kevin Garnett', 'John Havlicek*', 'Paul Pierce', 'Tim Duncan', 'Oscar Robertson*', 'Alex English*','Hakeem Olajuwon*', 'Elvin Hayes*', 'Allen Iverson*','Vince Carter',
 'Moses Malone*', 'Dominique Wilkins*', 'LeBron James', "Shaquille O'Neal*", 'Dirk Nowitzki', 'Michael Jordan*', 'Kobe Bryant', 'Wilt Chamberlain*', 'Karl Malone*','Kareem Abdul-Jabbar*'],
    ["#adb0ff", "#ffb3ff", "#90d595", "#e48381", "#aafbff", "#f7bb5f", "#eafb50","#adb0ff", "#ffb3ff", "#90d595", "#e48381", "#aafbff", "#f7bb5f", "#eafb50","#adb0ff", "#ffb3ff", "#90d595", "#e48381",  "#f7bb5f", "#eafb50"]))


def run_bar_chart(age):
    sf = table_20[table_20['Age'] == (age) ].sort_values(by='Total_PTS', ascending=True).tail(10)
    ax.clear()
    ax.barh(sf['Player'], sf['Total_PTS'], color=[colors[x] for x in sf['Player']])
    dx = sf['Total_PTS'].max() / 100
    for i, (Total_PTS, Player) in enumerate(zip(sf['Total_PTS'], sf['Player'])):
        ax.text(Total_PTS-dx, i,     Player,           size=14, weight=600, ha='right', va='bottom')
        ax.text(Total_PTS+dx, i,     f'{Total_PTS:,.0f}',  size=14, ha='left',  va='center')
    ax.text(1, 0.4, age, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Total points', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.15, 'The nba points leaders ',
            transform=ax.transAxes, size=24, weight=600, ha='left', va='top')
    ax.text(1, 0, 'by Marom Turel', transform=ax.transAxes, color='#777777', ha='right',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)

fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, run_bar_chart, frames=range(22, 41),interval=1200)
HTML(animator.to_jshtml())
plt.show()

