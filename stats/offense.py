import pandas as pd
import matplotlib.pyplot as plt

# Task 1
from data import games

plays = games[games['type'] == 'play']

plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# Task 2
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

# Task 3
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

# Task 4
replacements = {r'^S(.*)': 'single', r'^D(.*)': 'double', r'^T(.*)': 'triple', r'^HR(.*)': 'hr'}

# Task 5
hit_type = hits['event'].replace(replacements, regex=True)

# Task 6
hits = hits.assing(hit_type=hit_type)

# Task 7
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

# Task 8
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

# Task 9
hits = hits.sort_values(['inning', 'hit_type'])

# Task 10
hits = hits.pivot(index='inning', columns='hit_type', values='count')

# Task 11
hits.plot.bar(stacked=True)
plt.show()

