#http://www.seanlahman.com/baseball-archive/statistics/

from pybaseball import lahman as la
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
#remove chained assignment
#you can read more about chained assignment here: https://pandas.pydata.org/pandas-docs/version/0.22.0/indexing.html
pd.set_option('chained_assignment', None)

#setting these for later use
OAKLAND_PRIMARY_COLOR = '#003831'
OAKLAND_SECONDARY_COLOR = '#EFB21E'
STL_PRIMARY_COLOR = '#FF0000'
STL_SECONDARY_COLOR = '#0000FF'

# each of these functions gets us back a DataFrame.
salaries = la.salaries()
names = la.people()
teams = la.teams()
batting = la.batting()
home_games = la.home_games()

plt.style.use('seaborn-whitegrid')

salaries_teams_years = salaries.groupby(['teamID','yearID'], as_index = False).sum()

oak = salaries_teams_years.loc[salaries_teams_years['teamID'] == 'OAK']
stl = salaries_teams_years.loc[salaries_teams_years['teamID'] == 'SLN']

fig, ax = plt.subplots(figsize = (10, 7))

ax.plot(stl['yearID'], stl['salary']/1000000, label = 'STL', color = STL_SECONDARY_COLOR, linewidth = 1.5);
ax.plot(oak['yearID'], oak['salary']/1000000, label = 'OAK', color = OAKLAND_SECONDARY_COLOR, linewidth = 1.5);

# getting the line data for the Cardinals line plot
line_1 = ax.get_lines()[0].get_xydata()

# getting the line data for the Oakland A's lineplot
# ax.get_lines docs -> https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.get_lines.html
# this function returns a list of lines on the current axis.
# we can then call get xy_data() to get the x and y data
# line.get_xydata docs -> https://www.kite.com/python/docs/matplotlib.lines.Line2D.get_xydata
# it's in the form of a 2-dimensional Numpy Array, where the first column is the x data and the second column
# is the y data
line_2 = ax.get_lines()[1].get_xydata()

x_1, y_1 = line_1[:, 0], line_1[:, 1]
x_2, y_2 = line_2[:, 0], line_2[:, 1]

# fill the area underneath the curve for both Cardinals and A's
# ax.fill_between docs -> https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.fill_between.html
ax.fill_between(x_1, y_1, color = STL_PRIMARY_COLOR, alpha = 0.2)
ax.fill_between(x_2, y_2, color = OAKLAND_PRIMARY_COLOR, alpha = 0.2)

ax.set_xlabel('Year');
ax.set_ylabel('Team Salary in Millions',);
ax.set_title("Money Spent by Cardinals and A's", color = 'black');
ax.set_xlim([1985, 2016])

#prevent scientific notation
#reading: https://stackoverflow.com/questions/28371674/prevent-scientific-notation-in-matplotlib-pyplot
ax.ticklabel_format(useOffset = False)

ax.legend(loc = 'upper left');
plt.show()
