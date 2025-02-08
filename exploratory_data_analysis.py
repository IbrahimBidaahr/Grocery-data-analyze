#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# ## 1. Filtering

# In[2]:


import pandas as pd

groceries = pd.read_pickle('../Data/groceries_with_new_columns.pkl')
groceries.head()


# In[3]:


groceries.shape


# In[4]:


groceries.info()


# In[7]:


groceries.dtypes


# In[10]:


groceries.isna()


# In[11]:


groceries.isna().sum()


# In[2]:


# filter on low inventory
groceries[groceries['Low Inventory'] == 'Low Inventory']


# In[3]:


# compare with .loc
groceries.loc[groceries['Low Inventory'] == 'Low Inventory', ['Price_Dollars', 'Inventory']]


# In[4]:


# filter on the snacks subcategory
groceries[groceries.Subcategory == 'Snacks']


# In[5]:


# check one value
groceries.Subcategory[15]


# In[6]:


# strip then filter
groceries.Subcategory = groceries.Subcategory.str.strip()


# In[7]:


# filter on low inventory snacks
mask = (groceries['Low Inventory'] == 'Low Inventory') & (groceries.Subcategory == 'Snacks')
groceries[mask]


# In[8]:


# filter rows and columns
groceries.loc[mask, ['Subcategory', 'Item', 'Inventory']]


# ## 2. Sorting

# In[9]:


# filter on price
groceries.sort_values('Price_Dollars').head()


# In[10]:


# filter on price descending
groceries.sort_values('Price_Dollars', ascending=False).head()


# In[11]:


# sort on multiple columns
groceries.sort_values(['Subcategory', 'Price_Dollars']).head(10)


# In[12]:


# chain on sort_values
groceries[groceries['Low Inventory'] == 'Low Inventory'].sort_values('Price_Dollars')


# ## 3. Group By

# In[13]:


# group by category
groceries.groupby('Category')


# In[14]:


# group by category and show total inventory
groceries.groupby('Category')['Inventory'].sum()


# In[15]:


# group by category and unique items
groceries.groupby('Category')['Inventory'].count()


# In[16]:


# group by category and subcategory and unique items
groceries.groupby(['Category', 'Subcategory'])['Inventory'].count().reset_index()


# In[17]:


# group by category and subcategory and unique items
groceries.groupby(['Category', 'Subcategory'])['Inventory'].agg(['sum', 'count']).reset_index()


# In[18]:


# group by category and show max priced item
groceries.groupby('Category')['Price_Dollars'].max().reset_index()


# In[19]:


# group by category and show the item -- THIS IS INCORRECT!
groceries.groupby('Category')[['Item','Price_Dollars']].max()


# In[20]:


# this is correct
(groceries[['Category', 'Item', 'Price_Dollars']]
 .sort_values('Price_Dollars', ascending=False)
 .groupby('Category').head(1))


# ## 4. Pandas Plots

# In[21]:


groceries.head()


# In[22]:


# create a bar chart
groceries.groupby('Subcategory')['Price_Dollars'].mean().plot.bar();


# In[23]:


# create a horizontal bar chart
groceries.groupby('Subcategory')['Price_Dollars'].mean().plot.barh();


# In[24]:


# create a horizontal bar chart with sorted values
groceries.groupby('Subcategory')['Price_Dollars'].mean().sort_values().plot.barh();


# In[25]:


import pandas as pd

happiness = pd.read_csv('../Data/happiness_survey_data.csv')
happiness.head()


# In[26]:


# create a line chart for Mexico's happiness scores
happiness[happiness.country_name == 'Mexico'].iloc[:, 1:3].plot.line(x='year', y='happiness_score');


# In[27]:


# subset and pivot data to create multiple plots
(happiness[happiness.country_name.isin(['Canada', 'Mexico','United States'])]
                                 .iloc[:, :3]
                                 .pivot(index='year', columns='country_name', values='happiness_score'))


# In[28]:


# create a line chart with multiple lines
(happiness[happiness.country_name.isin(['Canada', 'Mexico','United States'])]
                                 .iloc[:, :3]
                                 .pivot(index='year', columns='country_name', values='happiness_score')
                                 .plot());


# ## 5. Pair Plot

# In[29]:


import seaborn as sns

student_data = pd.read_csv('../Data/student_data.csv')
student_data.head()


# In[30]:


sns.pairplot(student_data);


# ## 6. More Plots

# In[31]:


student_data['Cups of Coffee']


# In[32]:


# frequency table of discrete data
(student_data['Cups of Coffee'].value_counts()
                               .sort_index())


# In[33]:


# histogram
sns.histplot(student_data['Cups of Coffee'])


# In[34]:


# another histogram
sns.histplot(student_data['Cups of Coffee'],
             bins=10, color='purple');


# In[35]:


# frequency table of continuous data
student_data['Hours Studied'].round().value_counts().sort_index()


# In[36]:


# histogram of continuous data
sns.histplot(student_data['Hours Studied'])


# In[37]:


# scatter plot of data
sns.scatterplot(data=student_data, x='Hours of Sleep', y='Grade on Test')


# In[38]:


# digging into an outlier
student_data[student_data['Hours of Sleep'] < 3]


# In[39]:


# correlation table
student_data.corr()


# In[ ]:




