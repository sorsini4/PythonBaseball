"""
This is the data visualization part. This will allow us to see graphics of the data, rather then having to read through all the numbers.
Here on line 5 we see something that is usually non Pythonic, we have two statements on one line, seperated by a semicolon. This is how you can have
two statements on one line in python, otherwise this would be unattainable code.
"""
import pandas as pd; pd.set_option('display.max_columns', None)
import seaborn as sns
from matplotlib import pyplot as plt
import pybaseball as pyb
import warnings
warnings.filterwarnings('ignore')

#This sets a var data to the batting stats of 2019, then you copy the data to the batting var made on line 15, and then you print the first 5 entries.
data = pyb.batting_stats(2019)
batting = data.copy()
#print(batting.head(5))

"""
In the following code we will be printing 2019 stats for how many homers per at bats players have, we will filter out players with less than 50 ABs.
Many of these functions from seaborn consist of us having to pass in our DataFrames columns. In some cases we will only need to provide a single 
column, but in other cases where x/y data is required, we will provide two. 
First we will plot this data using seaborn, then we will do it in matplotlib. They do the same exact thing, but in some cases one is more useful than
the other. Usually matplotlib takes more lines of code to produce the same plot. They also look different, so you can choose whichever floats your boat

Seaborn documentation for scatter plots --->  https://seaborn.pydata.org/generated/seaborn.scatterplot.html
"""

#setting the style for visualizations
#sns.set_style('whitegrid')

#batting = batting[batting['AB'] > 50]

#setting figure size in inches
# link for documentation ---> https://matplotlib.org/3.3.0/api/_as_gen/matplotlib.pyplot.figure.html
#plt.figure(figsize = (8, 8))

#this line produces the plot, we input our x and y variables and set the title to make it look pretty
#sns.scatterplot(batting['AB'], batting['HR']).set_title('HR vs At Bats')

#this is a matplotlib func to show the plot
#plt.show()
 
"""
Now we are accomplishing the same thing as above, but with matplotlib instead of seaborn.
"""
#set figure size
#plt.figure(figsize = (8, 8))

#scatter plot our x and y
#plt.scatter(batting['AB'], batting['HR'])

#label axis and title
#plt.xlabel('AB')
#plt.ylabel('HR')
#plt.title('Homeruns vs At Bats', fontsize = 16)
#plt.show()

"""
Now we will look into Regression Plots. The available ones within seaborns library are 
    lmplot, regplot, & residplot
The purpose of these are to help you find a relationship between two variables. This usually involves trying to add a line of best fit to your data to try
and describe it. 
Firstly, we will look at regplot. Regplot plots your data and also adds a line of best fit. This is especially helpful considering we do not have to 
do this calculation of the line of best fit ourselves. Here we switch what were plotting to hits vs at bats to show you how well they correlate. We can 
draw a straight line through our data and it captures the data very well. This means you could predict how many hits a player gets if you knew how many
at bats he had. This is the very beginning  of LINEAR REGRESSION. 
We use plt from matplotlib we brought in earlier and used a function known as figure with a keyword argument of figsize. Although we must remember, seaborn
is an abstraction layer on top of matplotlib. Matplotlib is being used by us to adjust the knobs and dials of our visualization, while seaborn is taking
care of the heavy stuff like regression plots (statistical modeling) 

documentation for sns.regplot ---> https://seaborn.pydata.org/generated/seaborn.regplot.html
"""

#plt.figure(figsize = (12, 10))
#sns.regplot(batting['AB'], batting['H']).set_title('Hits vs At Bats')
#plt.show()

"""
Now we look into distribution plots. There are three distribution plots available to us through their API:
    rugplot, kdeplot, & distplot
The function distplot is a combination of a histogram plus a kernel density estimation. 
Lets plot some distibution plots for at bats. A distribution plot shows how many of your x variable you have in your data. The y-axis represents density,
in the form of a percentage. We see there is a peak of players with at bats around 100 and 500. We can probably say thqat the peak at 500 is from
everyday players. 
The bins in our distplot represent intervals of values, and seaborn is counting how many times a value in AB column falls within that interval. 
Essentially we are seeing a distribution of values here. You can adjust the number of bins to fine-grin the distribution by setting the bins 
argument to the distplot function we are using below. The graph that shows from the code below is a kernel density estimation, which is an attempt to 
plot the distribution of the data. We won't be covering the details of kernel density estimation, as the math is quite involved ***(look this up on your
own)***

documentation for kernel density ---> https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot
"""

#kernel density estimation for at bats
#plt.figure(figsize = (8, 8))
#sns.kdeplot(batting['AB'])
#plt.show()

"""
distplot for at bats

documentation for distplot ---> https://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot
"""

#plt.figure(figsize = (8, 8))
#sns.distplot(batting['AB'])
#plt.show()

#now we are doing it again to adjust the bins column
#plt.figure(figsize = (8, 8))
#sns.displot(batting['AB'])   #adjusting the bins column
#plt.show()

"""
Bivariate Kernel Density Estimation Plot
You can plot kernel density estimations for two dimensions by passing in two DF columns. 
Here, we can see the density estimation for two dimensions in one swoop. Let's plot the density estimation for hits and homers,
and also plot some notable players on the graph as well to see how they faired vs. the distribution.

We are going to use the object-oriented API for matplotlib to be able to have greater control over out plot. We can use the fig
and ax objects we get back from the plt.subplots function to annotate points for example.
https://matplotlib.org/3.3.0/api/_as_gen/matplotlib.pyplot.subplots.html

matplotlib Axes object documentation ---> https://matplotlib.org/3.3.0/api/axes_api.html

matplotlib Figure object documentation ---> https://matplotlib.org/3.3.0/api/_as_gen/matplotlib.figure.Figure.html 
"""


"""
fig, ax = plt.subplots(figsize = (10, 8))

notable_players = ['Mike Trout', 'Trea Turner', 'Chris Davis', 'Ronald Acuna Jr.']

for player_name in notable_players:
    player = batting.loc[batting['Name'] == player_name]
    
    if not player.empty:
        hits = player['H']
        homerun = player['HR']
        
        
        #plt.annotate documentation ---> https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.annotate.html
        

        ax.annotate(player_name, xy = (hits + 2, homerun + 2), color = 'red', fontsize = 12)
        ax.scatter(hits, homerun, color = 'red')

sns.kdeplot(batting['H'], batting['HR'], ax = ax) 
plt.show()

sns.jointplot(batting['H'], batting['HR'], kind = 'kde')
plt.show()
"""


"""
Residual Plots
Going back to the regression plot, seaborn also can plot residual plots. These essentially show us the difference between our regression model (the 
line of best fit) and the points on the x/y plane. This is important for data science and what we'll be doing in the machine learning sections. In the 
ML sections we will be fitting a line to some data. The more "bunched" together the data we are fitting the line to is around the line of best fit,
the better our line of best fit is actually fit. 

We are then going to take this line of best fit and use it to predict new values. These new values then get compared to real world values and the 
difference between the predicted value and then real world value is called residual. 

Analyzing the residuals of your model is an extremely important facet of modeling, and seaborn provides a quick helper function to plot the residuals
for a aline of best fit between two variables.

"""

 
"""
sns.set_style('dark')

sns.residplot(batting['AB'], batting['HR'])
plt.title('Residual Plot')
plt.xlabel('ABs')
plt.ylabel('Homers')
#saves the figure to the current directory
plt.savefig('foo.png')
"""


""" 
Understanding this graph:
Points bunched around the 0 part of our line indicate that our line of best fit perfectly matched up with an X, Y point on the plane. 

The x-axis represents our independent variable (or our input into the model), while the y-asix represents our residual. To reiterate, residual is how
wrong our line of best fit was. It is basically our error. The farther away a point is from the y = 0 line, the bigger our error. 

You can see as we got further and further away from 0, the distribution of our residual around the y-axis increased. This means that it got harder and
harder for our line of best fit to predict values as at bats got longer. When looking at residual plots, you want to ensure that the distribution of 
you residuals are relatively symmetrical along both axis's. If they aren't, then your model has room for improvement.

Points above the y-axis represent those points that our line of best fit overestimated a player's homeruns. Points below represent those points that
we underestimated. As you can see, the distribution along the y-axis is relatively equally distributed, but as we go along the x-axis, it does widen.
This indicates that further out in the player's with high number of at bats, there is something else that our model is missing that can predict homers,
(how much of a power hitter they are). For those players with a low amount of ABs, our model can accurately forecast their future performance.
"""



"""
Pairplot

This will show you a pair wise scatter plots (and regression plots, just set kind = 'reg' as a function keyword arg) for each column in your dataframe. 
This can be very useful when looking for two columns in your DataFrame that might be correlated. 

You might want to reduce the number of columns in your DataFrame before passing it in to the pairplot function as we did here with the batting_copy 
object, as the output is quite large if you have a decent amount of columns. 

For those cells where a column matches up with itself, pairplot returns a histogram of the results.

You can see by the pairplot below that stolen bases do not correlate well with any of hits, homeruns, or at bats.

"""
batting_copy = batting[['AB', 'H', 'HR', 'SB']]
sns.pairplot(batting_copy)
plt.show()


"""
Strike zone Application

Now that we got through the basics of plotting, lets apply this to an example where we plot the strike zone and pitch locations. Essentially we are taking the
variables plate_x and plate_z and plotting them. You can imagine our plot like you are looking at the pitcher from home plate and we are plotting where each
pitch is. So to do this we need to create out strike zone and it is also helpful to map each pitch type to a color so we can see if location changes
depending on the pitch type. 
"""

statcast = pyb.statcast(start_dt = '2020-09-22', end_dt = '2020-09-23')
print('{} Rows imported'.format(str(len(statcast))))

def plotPitches(plotdf):
    strikezone = plt.Rectangle((-.95, 1.6), 1.65, 1.8, color = 'red', fill = False)
    groups = plotdf.groupby("pitch_name")
    for name, group in groups:
        plt.plot(group["plate_x"], group["plate_z"], marker = "o", linestyle = "", label = name, alpha = .55)

    plt.ylim((0,5))
    plt.xlim((-3, 3))
    plt.gca().add_patch(strikezone)
    plt.legend(bbox_to_anchor = (1,1), loc = 'upper left', ncol = 1)

#find what pitchers are in the data, this will show us the top 10 pitchers by total pitches thrown
print(statcast.groupby('player_name', as_index = False)['pitch_type'].count().sort_values(by = 'pitch_type', ascending = False).head(10))

#pick a pitcher and isolate their pitches
cole = statcast[statcast['player_name'] == 'Gerrit Cole']

#plot pitchers pitches
plotPitches(cole)
plt.show()


#plot pitches thrown against right-handed batters
cole_vR = cole[cole['stand'] == 'R']
plotPitches(cole_vR)
plt.show()

#plot pitches thrown against left-handed batters
cole_vL = cole[cole['stand'] == 'L']
plotPitches(cole_vL)
plt.show()

#plot pitches thrown in certain counts
balls = 0
strikes = 2
cole_count = cole[(cole['strikes'] == strikes) & cole['balls'] == balls)]
plotPitches(cole_count)
plt.show()



























