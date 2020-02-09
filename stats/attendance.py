# Task 1
import pandas as pd
# Task 2
import matplotlib.pyplot as plt
# Task 3
from data import games
# Task 4
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]
# Task 5
attendance.columns = ['year', 'attendance']
# Task 6
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])
# Task 7 & 8 & 9
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance.attendance.mean(), label='Mean', linestyle='--', color='green')
plt.show()

