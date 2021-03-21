import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (12, 7))

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
plt.show()
