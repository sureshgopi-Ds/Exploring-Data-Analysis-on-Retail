#!/usr/bin/env python
# coding: utf-8

# # GRIP@TSF #Dec20

# # Task3:Exploratory Data Analysis - Retail

# # EDA using Pandas profiling

# In[21]:


import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport


# In[22]:


from pandas_profiling import ProfileReport


# In[23]:


filename='SampleSuperstore.csv'
data=pd.read_csv(filename)
data.head()


# In[24]:


# To create a simple report quickly
profile=ProfileReport(data,title='Pandas Profiling Report', explorative=True)


# In[25]:


profile.to_widgets()


# # Step1: Reading Data & Exploring

# In[14]:


import pandas as pd
df=pd.read_csv("SampleSuperstore.csv")#Reading csv files using pandas
df.head()#It shows 1st five rows


# In[16]:


df.tail()#It shows bottom five rows


# In[17]:


df.info()#It gives information of data and also it shows datatypes


# In[19]:


df.shape#It gives how many rows by columns


# In[20]:


df.describe()


# In[22]:


df.values


# In[23]:


df.columns


# In[24]:


df.index


# # Cleaning a Data

# In[3]:


import pandas as pd
df=pd.read_csv("SampleSuperstore.csv")
df.isnull().sum()


# # From above There is no null values in the dataset

# In[6]:


# Dropping the columns?
store=df.drop(['Region'],axis=1)


# In[7]:


store.head()


# In[9]:


store.duplicated().sum() #It show how many duplicates


# In[13]:


store.drop_duplicates(keep="first",inplace=True)
store.shape


# In[11]:


store.head()


# In[12]:


store.duplicated().sum()#checking if there is duplicates after dropping duplicates


# In[14]:


store.describe()# defining statistical values after duplicates are removed


# # Relational Analysis

# In[27]:


corr=store.corr()


# In[28]:


sns.heatmap(corr,annot=True,cmap='Greens')


# In[29]:


import seaborn as sns
import pandas as pd
df=pd.read_csv("SampleSuperstore.csv")
store=df.drop(['Region'],axis=1)
sns.pairplot(store,hue='Ship Mode')#pairplots are a great method to identify trends for follow-up analysis and it simply implemented in python


# In[30]:


sns.countplot(x=df['Ship Mode'])


# In[31]:


store['Segment'].value_counts()


# In[34]:


sns.pairplot(store,hue='Segment')


# In[35]:


sns.countplot(x='Segment',data=store,palette='rainbow')


# In[36]:


df['Category'].value_counts()


# In[40]:


sns.countplot(x='Category',data=store,palette='tab10')


# In[41]:


sns.pairplot(store,hue='Category')


# In[43]:


store['Sub-Category'].value_counts()


# In[45]:


plt.figure(figsize=(15,12))
store['Sub-Category'].value_counts().plot.pie(autopct='dark')
plt.show()


# # Observation 1:
#     #Maximum from Binders,paper,furnishing,phones,storsge,art,acessories and mimimum from copers,machines,supplies as shown in clearly above

# In[47]:


store['State'].value_counts()


# In[50]:


plt.figure(figsize=(15,12))
sns.countplot(x='State',data=store,palette='rocket_r',order=store['State'].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# # Observation 2
#     #Highest sales from california

# In[52]:


store.hist(figsize=(10,10),bins=50)
plt.show()


# # Observation 3
#     #Discount offers maximum 20%

# # Profit vs Discount

# In[57]:


fig,ax=plt.subplots(figsize=(20,8))
ax.scatter(store['Sales'],store['Profit'])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# In[58]:


sns.lineplot(x='Discount',y='Profit',label='Profit',data=store)
plt.legend()
plt.show()


# # Observation 4
#     No correlation between profit and discount

# # Profit vs Quantity

# In[59]:


sns.lineplot(x='Quantity',y='Profit',label='Profit',data=store)
plt.legend()
plt.show()


# In[62]:


store.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['green','yellow'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# # Observation 5
#      Profit and sales are maximum in consumer segment and mimimum in Home segment

# In[72]:


ps=df.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['pink','blue'],figsize=(15,8))
plt.title('Profit/Loss & Sales Across States')
plt.xlabel('States')
plt.ylabel('Profit/Loss & Sales')
plt.show()


# # Observation 6
#   profit states are california and New York,
#       loss states are Texas,ohio

# In[73]:


t_states =df['State'].value_counts().nlargest(10)
t_states


# In[75]:


df.groupby('Category')[['Profit','Sales']].sum().plot.bar(color=['pink','red'],alpha=0.9,figsize=(8,5))
plt.ylabel('Profit/Loss and Sales')
plt.show()


# # Observation 7
#   a)Technology and Pffice Supplies have high profit
#   b)Furniture have less Profit

# In[77]:


ps=df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['pink','blue'],figsize=(15,8))
plt.title('Profit/Loss & Sales Across States')
plt.xlabel('Sub-Category')
plt.ylabel('Profit/Loss & Sales')
plt.show()


# # Observation 8
#     Phones sub-category have high sales, Chairs have high sales but less profit compared to phones,Tables and Bookmarks sub-categories facing huge loss

# In[ ]:




