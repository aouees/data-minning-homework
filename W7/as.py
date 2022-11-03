# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# %%
df= pd.read_csv('WorldCups.csv')

# %%
df

# %%
df.info()

# %% [markdown]
# 😒😤DataType of 'Attendance' is object >> so we'll to convert to int64 💪

# %%
newdata=[]
for i in df['Attendance']:
    n=i.split('.')
    r=''
    for j in n:
        r+=j
    newdata.append(int(r))
df['Attendance']=newdata
df.info()

# %%
plt.plot(df['Year'],df['Attendance'],  marker='o')
plt.title('year vs Attendance for World Cups from 1930 to 2018', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Attendance', fontsize=14)
plt.show()

# %%
plt.scatter(df['QualifiedTeams'],df['GoalsScored'],color='red')
plt.title('Goals Scored vs number Qualified Teams for World Cups from 1930 to 2018', fontsize=14)
plt.ylabel('Goals Scored', fontsize=14)
plt.xlabel('Qualified Teams', fontsize=14)
plt.show()

# %%
plt.boxplot(df['Attendance'])
plt.show()

# %%
plt.hist(df['Winner'],bins=df['Winner'].size)
plt.title('How many Winner World Cups evrey Country', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('count', fontsize=14)
plt.show()

# %%
plt.pie(df['Winner'].value_counts(),labels= df['Winner'].value_counts().index.to_list()
,autopct='%1.2f%%')
plt.title('How many Winner World Cups evrey Country')
plt.show()

# %%

plt.bar(df['Country'],df['Attendance'],width=0.2)

plt.show()


# %%
pd.plotting.scatter_matrix(df)
plt.show()

# %%
sns.heatmap(df[df.corr().index].corr(),annot=True, cmap='RdYlGn')
plt.show()


