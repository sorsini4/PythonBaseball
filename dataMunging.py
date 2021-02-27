import pandas as pd
import numpy as np #importing numpy for future use
import matplotlib.pyplot as plt #also importing this for future use
import pybaseball as pyb
import seaborn as sns

pd.set_option('display.max_rows', None) #setting options for pandas to show all rows in DataFrames
pd.set_option('display.max_columns', None) #setting options for pandas to show all columns in DataFrames
pd.set_option('chained_assignment', None)

#this is how you view what version of pandas we are running
print(pd.__version__)

#2019 STATS
#print("2019 HITTING STATS")
#this is where we start using pybaseball 
df_2019 = pyb.batting_stats(2019)
#print(df_2019.head())

#this returns a tuple representing the dimensionality of the data fram
#print(df_2019.shape)

#print("2019 PITCHING STATS")
#df_2019 = pyb.pitching_stats(2019)
#print(df_2019.head())

#head will return the top, tail will return the bottom (5 if not specified)

#2020 STATS
print("2020 HITTING STATS")
df_2020 = pyb.batting_stats(2020)
#print(df_2020.head(5))
#another way to get first five rather than using head
#print(df_2020[:5])

"""
now we learn how to select certain columns from the df
this slices all the columns from the left side to WAR column, and then excludes anything after WAR
then the third statement is a nicer way to print out what columns we would see by joining them
"""
#df_2020 = df_2020.loc[:, :'WAR']
#print(df_2020.columns)
#print(', '.join(df_2020.columns))

"""
now we print only the specified columns with the following syntax, using slicing and loc
shows us the top 5 players according to WAR in 2020
"""
#print(df_2020.loc[:, ['Name', 'WAR']].head())

#shows us the bottom 5 players according to WAR in 2020
print(df_2020.loc[:, ['Name', 'WAR']].tail())

#finding stats for a specific team, using the df and loc
cards_df = df_2019.loc[df_2019['Team'] == 'Cardinals']
#print(cards_df.head())

#now we learn to sort by whichever statistic you would like
print(cards_df.sort_values(by = 'WAR', ascending = False).head(15))

#mariners_df = df_2020.loc[df_2020['Team'] == 'Mariners']
#print(mariners_df.head())

"""
We can use the describe method to get summary and descrptive stats about of DF very quickly
We can also use transpose to switch the columns and index
"""
#print(cards_df.describe().transpose().head(10))

"""
This is how you get a series object, or column from your dataframe
here we just get the first 10 rows of the series object
"""
#print(cards_df['H'][:10])

"""
there are many different functions you can use on series, such as min, max, std (standard deviation),
and quantile (which will show to percentile of the specified parameter). These are all demonstrated
below.
"""
#max of hits in series
print(cards_df['H'].max())
#min of hits in series
print(cards_df['H'].min())
#standard deviation of hits in series
print(cards_df['H'].std())
#quantile of 75th percentile of hits in series
print(cards_df['H'].quantile(.75))

"""
The value_counts is a series method which can be used to find the number of occurences in a column
***for some reason this is only doing the head (first 5)***
"""
print(cards_df['Age'].value_counts())


"""
We can also visualize this data in the same fashion. 
we NEED the plt.show() function, as it is necessary for the graphic to show up
"""
#sns.set_style('whitegrid')
#sns.displot(cards_df['Age'].astype(int));
#plt.show()

#goldy = cards_df.loc[cards_df['Name'] == 'Paul Goldschmidt']
#goldy = goldy.transpose()
#goldy.index = goldy.index.rename('Category')

#goldy.columns = ['Value']
#print(goldy.head(10))

"""
The rank method can be used to rank players based on a given column
Set ascending = False to rank the column in DESCENDING order
With this below 2 lines of code we are making a new column within the table,
the syntax of it is 
    ** df['new_column_name'] = df['old_column'].method() **
we are in the below code locating the AVG column, and then using the rank method to rank them from
least to most (descending order, highest to lowest) 
"""
cards_df['AVGRank'] = cards_df['AVG'].rank(ascending = False)
print(cards_df.sort_values(by = 'AVGRank').head(10))

""""
You can build upon the above code by adding batting requirements, such as at bats etc.
In the third line of code, we learn about the groupby method. The goal is to find the total WAR for each
MLB team. Essentially, groupby allows us to aggregate our data into groups. The first example is showing 
how many times each team walked in the year 2019.
"""
#df_2019 = df_2019.loc[df_2019['AB'] > 100]
#print(df_2019)
print(df_2019.groupby('Team')['BB'].sum())

"""
Now we are doing the same thing, but with WAR of the top three guys on the team
"""
team_batting_WAR_2019 = df_2019.groupby('Team')['WAR'].apply(lambda group: group.nlargest(3).sum())
team_batting_WAR_2019 = team_batting_WAR_2019.reset_index()
print(team_batting_WAR_2019)

"""
In the previous table we had a '---' with a WAR number next to it. This is the players that were on two
teams throughout the season. So lets take them out
"""
team_batting_WAR_2019 = team_batting_WAR_2019.loc[team_batting_WAR_2019['Team'] != '---']
print(team_batting_WAR_2019.sort_values('WAR', ascending = False).head(5))


"""
Next we will work on merging two DataFrames. This is very common, and is important when you have info
in two different places that you want to use together. In the below code, we have our WAR DataFrame and 
want to see how it correlates to team wins. Although, we do not have a team wins DataFrame. Luckily, 
pybaseball has a standings attribute we can pull the season standings from any year. So we will pull from
2019 and clean it up. 
The standings data is a list of DataFrames broken up by division. For our purpose we want to use it as one 
DataFrame so we are going to use a loop to append them all together, then we will have the Wins DataFrame
which will show the standings for each individual team.
"""

standings = pyb.standings(2019)

wins = pd.DataFrame()

#we are using pd.concat to iteratively update our DataFrame
for division_df in standings:
    wins = pd.concat([wins, division_df])

wins = wins.rename({'Tm': 'Team'}, axis = 1)

#print(wins)

"""
The problem with the above code, is when you are merging the two DataFrames, it won't know that the 
Los Angeles Dodgers, and Dodgers are the same, so we need to use str.split() in order to fix this. 
Although, we run into another problem with team names like the Blue Jays, and White/Red Sox. We use iloc
to be able to fix this porition of the problem.
"""

#this is known as a vectorized string operation
#saving this to the team column of wins DF, take the last element of the str (index -1)
wins['Team'] = wins['Team'].str.split().str[-1]

wins = wins.reset_index(drop = True)

#manually adjusting the individual cells (For above anomallies)
wins.iloc[3, 0] = 'Blue Jays'
wins.iloc[2, 0] = 'Red Sox'
wins.iloc[7, 0] = 'White Sox'

print(wins.head(30))

"""
Now we merge! This is a simple command with the syntax 
***             first_df.merge(second_df, on = "column_name_youre_merging_on")              ***
The column you merge on means how you want to match up your DataFrames. Since we picked teams python 
is going to go through both our DF's and match the rows together where necessary (same team name). This
is exactly what we want.
"""

team_batting_WAR_2019 = team_batting_WAR_2019.merge(wins, on = "Team")
print(team_batting_WAR_2019)

"""
Now we are going to convert our data types into floats since you cannot plot them as strings (you can,
they just would not be in numeric order)
"""

columns = ['W', 'WAR']

#astype formats an entire column as a given data type
for column in columns:
    team_batting_WAR_2019[column] = team_batting_WAR_2019[column].astype('float')

"""
We are repeating the process above for the following cases, the top 4 and 9 players on 
the team. This will help us find out whether its more important to have the well rounded
team or a couple of superstars. 
"""

plt.style.use('fivethirtyeight')

#repeating above steps with n = 9
team_batting_WAR_2019 = df_2019.groupby('Team', as_index = False)['WAR'].apply(lambda group: group.nlargest(9).sum())

team_batting_WAR_2019 = team_batting_WAR_2019.loc[team_batting_WAR_2019['Team'] != '---']
team_batting_WAR_2019 = team_batting_WAR_2019.merge(wins, on = 'Team')

columns = ['W', 'WAR']

#Plotting
for column in columns: 
    team_batting_WAR_2019[column] = team_batting_WAR_2019[column].astype('float')

x = team_batting_WAR_2019['WAR']
y = team_batting_WAR_2019['W']

#grab a line of best fit
m, b = np.polyfit(x.values, y.values, 1)

plt.figure(figsize = (15, 10))

plt.scatter(x, y)
plt.plot(x, x * m + b)

plt.title('Wins vs WAR of Top 9 Players', fontsize = 16)
plt.xlabel('WAR')
plt.ylabel('Team Wins')

ax = plt.gca()

for _, row in team_batting_WAR_2019.iterrows():
    ax.annotate(row['Team'], xy = (row['WAR'], row['W']))

plt.show()

"""
Now doing it for the top 4 players rather than the top 9
Same code just changing line 263 to group.nlargest(4) instead of (9)
"""
plt.style.use('fivethirtyeight')

#repeating above steps with n = 9
team_batting_WAR_2019 = df_2019.groupby('Team', as_index = False)['WAR'].apply(lambda group: group.nlargest(4).sum())

team_batting_WAR_2019 = team_batting_WAR_2019.loc[team_batting_WAR_2019['Team'] != '---']
team_batting_WAR_2019 = team_batting_WAR_2019.merge(wins, on = 'Team')

columns = ['W', 'WAR']

#Plotting
for column in columns: 
    team_batting_WAR_2019[column] = team_batting_WAR_2019[column].astype('float')

x = team_batting_WAR_2019['WAR']
y = team_batting_WAR_2019['W']

#grab a line of best fit
m, b = np.polyfit(x.values, y.values, 1)

plt.figure(figsize = (15, 10))

plt.scatter(x, y)
plt.plot(x, x * m + b)

plt.title('Wins vs WAR of Top 9 Players', fontsize = 16)
plt.xlabel('WAR')
plt.ylabel('Team Wins')

ax = plt.gca()

for _, row in team_batting_WAR_2019.iterrows():
    ax.annotate(row['Team'], xy = (row['WAR'], row['W']))

plt.show()


