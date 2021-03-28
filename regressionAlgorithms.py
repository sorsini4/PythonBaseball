import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pybaseball as pyb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from pybaseball import cache

cache.enable()

fig, ax = plt.subplots(figsize = (12, 7))

"""
#creating the df
df = pd.DataFrame({
    'hits_last_year': [120, 180, 105, 133, 150],
    'abs_last_year': [400, 560, 450, 505, 490],
    'hits_next_year': [127, 170, 110, 128, 145]})

#printing the df
print(df.head())

#styling the graph
sns.set_style('whitegrid')
ax.set_title('Projecting Hits')
ax.set_ylabel('Projected Hits')
ax.set_xlabel('Last Years Hits')

sns.regplot(data = df, x = 'hits_last_year', y = 'hits_next_year')
#plt.show()
"""

#predicting hits section
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('chained_assignment', None)

print('Loading ten years of data...this may take a few minutes')

#loading df from 2010-2020
hits_df = pyb.batting_stats(2010, 2021)
hits_2019 = pyb.batting_stats(2018, 2019)

print('data loaded')

hits_df_copy = hits_df.copy()

hits_df_copy = hits_df_copy.loc[:, ['Season', 'Name', 'AB', 'HR', 'SLG', 'LD%', 'wOBA', 'Contact%', 'Soft%', 'Med%', 'Hard%']]

hits_df_copy['HR_Next_Year'] = hits_df_copy.sort_values(['Name', 'Season'], ascending = False).groupby('Name')['HR'].shift()

hits_df_copy = hits_df_copy.loc[hits_df_copy['AB'] > 300] 

hits_df_copy = hits_df_copy.loc[hits_df_copy['HR_Next_Year'].notnull()]

print(hits_df_copy.loc[hits_df_copy['Name'] == 'Mike Trout', ['Season', 'Name', 'AB', 'HR', 'SLG', 'LD%', 'wOBA', 'Contact%', 'Soft%', 'Med%', 'Hard%', 'HR_Next_Year']].sort_values(by = 'Season'))

print(hits_df_copy.corr()[['HR_Next_Year']].sort_values(by = 'HR_Next_Year', ascending = False))

#starting the machine learning portion to predict hits
x = hits_df_copy[['AB', 'HR', 'SLG', 'LD%', 'wOBA', 'Contact%', 'Soft%', 'Med%', 'Hard%']].values
y = hits_df_copy[['HR_Next_Year']].values

print('Original Data Shape - X: {0}, Y: {1}'.format(x.shape, y.shape))

#split up our data into 20% testing, 80% training
#train_test_split documentation --> https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 42, test_size = 0.2)

print('Train Data Shape - X: {0}, Y: {1}'.format(x_train.shape, y_train.shape))
print('Test Data Shape - X: {0}, Y: {1}'.format(x_test.shape, y_test.shape))

#LinearRegression class documentation -->  https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
#Fit method documentation --> https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit
lr = LinearRegression()

print('fitting data...')

lr.fit(x_train, y_train)

"""
Predicted values based off testing data. We are going to compare these predicted values to real world values
and try to quantify the difference between our model and reality.
predict method documentation --> https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict
mean_absolute_error documentation --> https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html
So below we will predict on x_train using the predict method and check the error between our predicted and the actual values which are y_train here. Training data is always
matched with training data. 
"""
y_pred = lr.predict(x_train)

print('Mean number of hits:', x_train[:, 0].mean())
print('Mean absolute error:', mean_absolute_error(y_pred, y_train))

#Testing the model on the 2019 season
hits_2019_copy = hits_2019.copy()
hits_2019_copy = hits_2019_copy.loc[:, ['Season', 'Name', 'AB', 'HR', 'SLG', 'LD%', 'wOBA', 'Contact%', 'Soft%', 'Med%', 'Hard%']]
hits_2019_copy['2019_actual_hrs'] = hits_2019_copy.sort_values(['Name', 'Season'], ascending = False).groupby('Name')['HR'].shift()
hits_2019_copy = hits_2019_copy.loc[hits_2019_copy['AB'] > 300]
hits_2019_copy = hits_2019_copy.loc[hits_2019_copy['2019_actual_hrs'].notnull()]

x = hits_2019_copy[['AB', 'HR', 'SLG', 'LD%', 'wOBA', 'Contact%', 'Soft%', 'Med%', 'Hard%']].values
y = hits_2019_copy[['2019_actual_hrs']].values

y_pred = lr.predict(x)
print('Mean number of homers:', hits_2019_copy['HR'].mean())
print('Mean absolute error:', mean_absolute_error(y_pred, y))

hits_2019_copy['Predicted_Homers'] = y_pred
hits_2019_copy['Season'] = 2019
hits_2019_copy = hits_2019_copy.rename(columns = {'2019_actual_hrs': 'Actual_Hrs'})

#use sort_values to find the top predicted hits
print(hits_2019_copy.loc[:, ['Season', 'Name', 'Actual_Hrs', 'Predicted_Homers']].head(50))

























