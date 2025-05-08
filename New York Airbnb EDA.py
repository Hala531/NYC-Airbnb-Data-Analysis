#!/usr/bin/env python
# coding: utf-8

# # **New York Airbnb EDA Project**

# **Steps** 
# 1. Importi ng all dependencies
# 2. Loadind datasets
# 3. initial exploration
# 4. Data cleaning
# 5. Data analysisd
#    

# 1. **Importing all dependencies** 

# In[3]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# 2. **Loading Datasets**

# In[4]:


#load csv file from local path 
df = pd.read_csv("C:/Users/HP/Downloads/datasets.csv")  
#Display the first 5 rows of the dataset 


# 3. **Initial Exploration** 

# In[5]:


df.head()


# In[17]:


df.tail()


# In[9]:


df.shape


# In[11]:


df.info()


# In[13]:


##Statistical summary
df.describe()


# 4. **Data Cleaning**

# In[15]:


df.isnull().sum()


# In[17]:


#Dropping all missing values rows 
df.dropna(inplace = True)


# In[19]:


df.isnull().sum() 
# Now all the missing Values are gone 


# In[21]:


df.shape


# In[23]:


# Dealing with Duplicate rows 
df.duplicated().sum()


# In[25]:


# The rows that are duplicated 
df[df.duplicated()]


# In[31]:


#Deleting all duplicate records 
df.drop_duplicates(inplace = True) 


# In[33]:


df.duplicated().sum() df['id']


# In[35]:


df.dtypes


# In[37]:


#type casting 
#changing data types 
df['id'] = df['id'].astype(object)
df['host_id'] = df['host_id'].astype(object)
df.dtypes


# #### EDA
# 

# 5. **Data Analysis** 

# **Univariate Analysis** (Analysing single comlumns and their Sata Distributions)

# In[39]:


#identifying outliers in price (boxplot is used for identifying sns)
sns.boxplot(data = df, x = 'price') 
#we can see that most of the prices are spreading between 0 and maybe 17000 and maybe one or two prices are at 100000 which is causing the issue 



# In[41]:


#dealing with outliers 
data = df[df['price'] < 1500] 
sns.boxplot(data = data, x= 'price') #now we can see there are the maximum price that are relying, there are less chances of getting outliers because the prices are spreaded equally


# In[43]:


plt.figure(figsize=(8,5))
sns.histplot(data = data, x = 'price')
plt.title('Price Distribution') 
plt.ylabel("Frequency")
plt.show()


# In[45]:


plt.figure(figsize=(6, 3)) 
sns.histplot(data = data , x = 'availability_365') 
plt.title ('availability_365 Distribution')  
plt.ylabel("Frequency") 
plt.show()


# In[134]:


data.groupby(by='neighbourhood_group')['price'].mean()


# In[47]:


data.head()


# **Feature Engineering**

# In[56]:


data = data.copy()
data['price per bed'] = data['price'] / data ['beds']


# In[58]:


data.head()


# In[60]:


data.groupby(by = 'neighbourhood_group')['price per bed'].mean()


# **Bi Variable Analysis**

# In[67]:


## One variable dependency in another variable 'How one column affact another column'
data.columns


# In[73]:


##Price dependencies on neighbourhood
sns.barplot(data = data, x = 'neighbourhood_group', y = 'price', hue = 'room_type')


# In[85]:


## number of reviews and price relationship 
plt.figure(figsize = (8, 5)) 
plt.title ("Locality and Review dependency")
sns.scatterplot(data = data, x = 'number_of_reviews', y = 'price', hue = 'neighbourhood_group') 
plt.show()
## we notice that the most of the reviews that we are getting is for this range where the price is maybe somewhere  around 600 $ and 10$


# In[87]:


data.dtypes 


# In[96]:


#creating a plot between all numerical columns 
sns.pairplot(data = data, vars = ['price', 'minimum_nights', 'number_of_reviews', 'availability_365', ], hue = 'room_type')


# In[106]:


##Geographical distribution of Airbnb listings 
plt.figure(figsize = (10, 7))
sns.scatterplot(data = data, x = 'longitude', y = 'latitude', hue = 'room_type') 
plt.title("Geographical distribution of Airbnb listing")
plt.show()


# In[114]:


data.dtypes


# In[116]:


## heat map - correlation of one variable with others for numerical columns 
corr = data[['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'beds']].corr()
corr


# In[122]:


plt.figure(figsize = (8, 6))
sns.heatmap(data = corr, annot = True )## annote = true to see the values 


# In[ ]:




