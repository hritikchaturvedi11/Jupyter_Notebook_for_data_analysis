#!/usr/bin/env python
# coding: utf-8

# import panda

# In[1]:


import pandas as pd


# Import Data

# In[2]:


names = ['Id','Title', 'Year', 'Rating', 'Votes', 'Length', 'Generes']
data = pd.read_csv('imdb_top_10000.txt', sep='\t', names=names, index_col = 0)


# Exploring the data

# In[3]:


data


# In[25]:


data.head


# In[26]:


data.head(3)


# In[27]:


data.tail()


# In[28]:


data.info()


# In[29]:


data.describe()


# In[3]:


data.to_csv('text.csv', header = True, index = True, sep = ',')


# In[4]:


data.to_csv('test.csv', header=True, index=True, sep=',')


# Sorting Data

# In[6]:


data.sort_values(by='Rating')


# Sort in ascending order

# In[8]:


data.sort_values(by='Rating', ascending=False)


# Creating Data Frames from scratch

# In[9]:


sample_data = {
   'tv': [230.1, 44.5, 17.2],
   'radio': [37.8, 39.3, 45.9],
   'news': [69.2, 45.1, 69.3],
   'sales': [22.1, 10.4, 9.3]
}


# In[11]:


data2 = pd.DataFrame(sample_data)


# In[12]:


data2


# In[13]:


del data2


# In[15]:


data2 = pd.DataFrame(sample_data)


# In[16]:


data2


# In[17]:


del data2


# selecting Data

# In[33]:


data[['Title','Year']]


# In[35]:


data['Rating'].mean()


# In[36]:


data['Rating'].min()


# In[37]:


data['Rating'].max()


# In[38]:


data['Rating'].median()


# In[39]:


data['Rating'].mode()


# In[40]:


data['Generes'].unique()


# In[41]:


data['Generes'].unique()


# In[47]:


rate = data['Rating'].value_counts()


# In[49]:


rate.sort_values()


# In[50]:


data['Rating'].value_counts().sort_index()


# In[52]:


data['Rating'].value_counts().sort_index(ascending = False)


# Import Matplotlib inline for curves

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


data.plot()


# In[56]:


data


# In[57]:


data.plot()


# In[58]:


data.plot.line()


# In[59]:


data.plot(kind='line')


# Vertical Bar Graph

# In[61]:


data.plot(kind='bar')


# Histogram

# In[62]:


data.plot.hist()


# Horizontal Bar 

# In[64]:


data.plot.barh()


# In[65]:


data.plot(kind='box')


# In[67]:


data.plot(kind='area')


# In[74]:


data.plot(kind='scatter', x='Rating', y='Votes')


# In[75]:


data.plot.hexbin(x='Rating', y='Votes')


# Import Seaborn

# In[6]:


import seaborn as sns


# In[7]:


sns.pairplot(data)


# In[10]:


sns.lmplot(x='Rating', y='Votes', data=data)


# In[11]:


sns.lmplot(x='Year',y='Votes',data=data)


# Ordinary Least Square(OLS) Regression

# In[7]:


import statsmodels.api as sm


# In[8]:


results = sm.OLS(data['Rating'],data['Votes']).fit()


# In[9]:


results.summary()


# In[20]:


print('Parameters: ', results.params)
print('R2: ', results.rsquared)


# In[21]:


print('Standard Erors: ',results.bse)


# In[23]:


print('Predicted Values: ',results.predict())


# Advanced Data selection

# In[26]:


data[data['Year']>1995]


# In[28]:


data[data['Rating']==9.0]


# In[30]:


data[data['Rating']==9.2 ]


# In[31]:


data['Rating']==9.2


# In[37]:


data[(data['Year'] > 1995) & (data['Year'] < 2000)]


# In[38]:


data[(data['Year'] > 1995) & (data['Rating'] < 9)]


# In[40]:


data[(data['Year'] > 1995) | (data['Year'] < 2000)]


# Sorting and applying conditions and giving only 10 results

# In[43]:


data[(data['Year'] > 1995) & (data['Year'] < 2000)].sort_values(by='Rating', ascending=False).head(10)


# In[44]:


data[(data['Rating']>8) & (data['Year']==1998)].sort_values(by='Votes', ascending=False).head(3)


# Group By in Pandas

# In[45]:


data.groupby(data['Rating'])


# In[46]:


data.groupby(data['Rating'])['Rating'].mean()


# In[50]:


data.groupby(data['Year'])['Year'].mean()


# In[52]:


data.groupby(data['Year'])['Year'].median()


# In[54]:


data.groupby(data['Year'])['Year'].mean().sort_values(ascending=False).head(10)


# In[59]:


data.groupby(data['Rating'])['Rating'].mean().sort_values(ascending=False).head(-50)


# In[61]:


data.groupby(data['Year'])['Rating'].mean()


# In[62]:


data.groupby(data['Year'])['Rating'].mean().sort_values(ascending=False).head(50)


# In[64]:


data.groupby(data['Year'])['Rating'].max().sort_values(ascending=False).head(1)


# In[66]:


data['Title']


# In[69]:


data.groupby(data['Title'])['Rating'].max().sort_values()


# In[70]:


data.groupby(data['Title'])['Rating'].max()


# In[73]:


data.groupby(data['Title'])['Votes'].max().sort_values(ascending=False).head(5)


# In[ ]:




