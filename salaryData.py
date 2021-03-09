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
OAK_PRIMARY_COLOR = '#003831'
OAK_SECONDARY_COLOR = '#EFB21E'
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

ax.plot(stl['yearID'], stl['salary']/1000000, label = 'STL', color = STL_SECONDARY_COLOR, linewidth = 1.5)
ax.plot(oak['yearID'], oak['salary']/1000000, label = 'OAK', color = OAK_SECONDARY_COLOR, linewidth = 1.5)

# getting the line data for the Cardinals, A's, and line plot
# ax.get_lines docs -> https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.get_lines.html
# this function returns a list of lines on the current axis.
# we can then call get xy_data() to get the x and y data
# line.get_xydata docs -> https://www.kite.com/python/docs/matplotlib.lines.Line2D.get_xydata
# it's in the form of a 2-dimensional Numpy Array, where the first column is the x data and the second column
# is the y data
line_one = ax.get_lines()[0].get_xydata()
line_two = ax.get_lines()[1].get_xydata()

x_one, y_one = line_one[:, 0], line_one[:, 1]
x_two, y_two = line_two[:, 0], line_two[:, 1]

# fill the area underneath the curve for both Cardinals and A's
# ax.fill_between docs -> https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.fill_between.html
ax.fill_between(x_one, y_one, color = STL_PRIMARY_COLOR, alpha = 0.2)
ax.fill_between(x_two, y_two, color = OAK_PRIMARY_COLOR, alpha = 0.2)

ax.set_xlabel('Year');
ax.set_ylabel('Team Salary in Millions',);
ax.set_title("Money Spent by Cardinals and A's", color = 'black');
ax.set_xlim([1985, 2016])

#prevent scientific notation
#reading: https://stackoverflow.com/questions/28371674/prevent-scientific-notation-in-matplotlib-pyplot
ax.ticklabel_format(useOffset = False)

ax.legend(loc = 'upper left');
plt.savefig('salaryDataForCardsAndAs.png')
plt.show()


#looking at the cardinals top 10 years in payroll 
print(stl.sort_values(by = 'salary', ascending = False).head(10))

#wins vs money spent: The cardinals obviously spent more than the A's, but did the money spent translate to wins?
salaries_teams_years = salaries.groupby(['teamID', 'yearID'], as_index = False).sum()
print(salaries_teams_years.sort_values(by = 'salary', ascending = False).head(10))

#stl_wins = money_wins[(money_wins['teamID'] == 'SLN') & (money_wins['W'] > 90)]

money_wins = salaries_teams_years.merge(teams, on = ['teamID', 'yearID'])
oak_stl = money_wins[(money_wins['teamID'] == 'OAK') | (money_wins['teamID'] == 'SLN')]

oak_stl['salary/win'] = oak_stl['salary'] / oak_stl['W']

plt.style.use('ggplot')

oak = oak_stl.loc[oak_stl['teamID'] == 'OAK']
stl = oak_stl.loc[oak_stl['teamID'] == 'SLN']

fig, ax = plt.subplots(figsize = (10, 8))

#setting the s keyword arg to make point size a function of team W's -> the more wins you had as a team, the bigger the point is going to be on the graph
ax.scatter(x = oak['yearID'], y = oak['salary/win'], color = OAK_PRIMARY_COLOR, alpha = 0.6, edgecolors = OAK_SECONDARY_COLOR, linewidth = 1.5, s = oak['W'] * 1.5)
ax.scatter(x = stl['yearID'], y = stl['salary/win'], color = STL_PRIMARY_COLOR, alpha = 0.6, edgecolors = STL_SECONDARY_COLOR, linewidth = 1.5, s = stl['W'] * 1.5)

#preventing scientific notation again
ax.ticklabel_format(useOffset = False)

ax.set_xlim([1985, 2016])
ax.set_ylim(0)
ax.set_xlabel('Year')
ax.set_ylabel('Dollar Spent per Win')
ax.set_title('Oakland and St. Louis\'s dollars spent per win')

plt.legend(['OAK', 'STL'], loc = 'upper left')
fig.text(0.8, -.05, 'Point size is a function of team wins', ha = 'center')

plt.show()
plt.savefig('WinsVsMoneySpent.png')






































