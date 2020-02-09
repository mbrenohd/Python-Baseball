# Task 1
import os
import glob
# Task 2
import pandas as pd

# Task 3
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
# Task 4
game_files.sort()

# Task 5 & 6
game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)
# Task 7
games = pd.concat(game_frames)
# Task 8
games.loc['??', ['multi5']] = ''
# Task 9
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
# Task 10
identifiers = identifiers.fillna(method='ffill')
# Task 11
identifiers.columns(['game_id', 'year'])
# Task 12
games = pd.concat([games, identifiers], axis=1, sort=False)
# Task 13
games = games.fillna(' ')
# Task 14
games.loc[:, ['type']] = pd.Categorical(games.loc[:, ['type']])
# Task 15
games.head()
