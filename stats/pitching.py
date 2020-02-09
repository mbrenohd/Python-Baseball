import pandas as pd
import matplotlib.pyplot as plt
# Task 1
from data import games
plays = games[games['type'] == 'play']

# Task 2
strikes_outs = plays[plays['event'].str.contains('K')]

# Task 3
strikes_outs = strikes_outs.groupby(['year', 'game_id']).size()

# Task 4
strikes_outs = strikes_outs.reset_index(name='strike_outs')

# Task 5
strikes_outs = strikes_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

#Task 6
strikes_outs.plot(x='year', y='strike_outs', kind='scatter')
plt.legend('Strike Outs')
plt.show()








