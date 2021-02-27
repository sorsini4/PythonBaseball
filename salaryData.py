from pybaseball import lahman as la
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
#remove chained assignment --> documentation https://pandas.pydata.org/pandas-docs/version/0.22.0/indexing.html
pd.set_option('chained_assignment', None)

#setting these for later use
OAKLAND_PRIMARY_COLOR = '#003831'
OAKLAND_SECONDARY_COLOR = '#EFB21E'
NYY_PRIMARY_COLOR = '#003087'
NYY_SECONDARY_COLOR = '#E4002C'

#each of these functions gets us back a data frame!
salaries = la.salaries()
names = la.people()
teams = la.teams()
batting = la.batting()
home_games = la.home_games()

salaries_years = salaries.groupby('yearID', as_index = False).sum()
print(salaries_years.head(10))

#list of styling options -> https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html

plt.style.use('seaborn-darkgrid')
year_id = salaries_years['yearID']
salary = salaries_years['salary'] / 1e9

fig, ax = plt.subplots(figsize=(10,8))

ax.plot(year_id, salary)
ax.set_xlabel('Year', color = 'black')
ax.set_ylabel('Dollars in billions', color = 'black')
ax.set_title('Money spent in the MLB', color = 'black')
plt.show()

