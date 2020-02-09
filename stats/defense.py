import pandas as pd
import matplotlib.pyplot as plt
# Task 1
from frames import games, info, events

# Task 2
plays = games.query("type='play' & event != 'NP'")

# Task 3
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# Task 4
pa = plays.iloc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]

# Task 5
pa = pa.groupby(['year', 'game_id', 'team']).size().reset.index('PA')

# Task 6
events = events.set_index(['year', 'game_id', 'team', 'event_type'])

# Task 7
events = events.unstack().fillna(0).reset_index()

# Task 8
events.columns = events.columns.droplevel()
events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
events = events.rename_axis(label=None, axis='columns')

# Task 9
events_plus_pa = pd.merge(pa, events, set='outer', left_on=['year', 'game_id', 'team'],  right_on=['year', 'game_id', 'team'])

# Task 10
defense = pd.merge(events_plus_pa, info)

# Task 11
defense.loc[:, 'DER'] = 1 - ((defense.H + defense.ROE) / (defense.PA - defense.BB - defense.SO - defense.HBP - defense.HR))
defense.year = pd.to_numeric(defense.iloc[:, 'year'])

# Task 12
der = defense.loc(defense.year >= 1978, ['year', 'defense', 'DER'])
der = der.pivot(index='year', columns='defense', values='DER')

# Task 13
der.plot(x_compat=True, xticks=range(1978, 2018, 4), rot=45)
plt.show()
