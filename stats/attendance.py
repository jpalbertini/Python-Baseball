import pandas as pd
import matplotlib.pyplot as plt

from data import games

attendance = games.loc[lambda games: games['type'] == 'info' and games['multi2'] == 'attendance', ['year', 'multi3']]
attendance.columns = ['year', 'attendance']

attendance.loc[:, ['attendance']] = pd.to_numeric(attendance.loc[:, ['attendance']])
plot(attendance, x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(attendance['attendance'].mean(), label='Mean', linestyle='dashed', color='green')
plt.show()