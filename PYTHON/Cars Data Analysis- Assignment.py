#!/usr/bin/env python
# coding: utf-8

# # Cars Dataset Analysis
# -Condition
# -Function
# -loop

# In[1]:


import pandas as pd


# In[2]:


cars=pd.read_csv('cars.csv')


# In[3]:


cars.columns


# In[4]:


cars.head()


# ## 1- How many Rows are in the cars dataset?

# In[5]:


cars.shape[0]


# ## 2- How many Columns are in the car's data set?

# In[6]:


cars.shape[1]


# ## 3- How many unique numbers of cylinders we have in the cars dataset?

# In[7]:


cars.cylenders.value_counts()


# In[8]:


cars.cylenders.unique()


# ## 4- What is the average horsepower of cars? 

# In[9]:


cars.horsepower.describe()


# In[12]:


cars.horsepower.mean()


# ## 5- What is the maximum horsepower?

# In[14]:


cars.horsepower.max()


# ## 6- What is the most expensive car ?

# In[15]:


cars[cars.Price== max(cars.Price)]


# In[16]:


most_expensive_car = cars[cars['Price'] == cars['Price'].max()]


# In[17]:


most_expensive_car


# 7- change the name of the column "name" to "car name"

# In[18]:


cars= cars.rename(columns= {'name': 'car_name'})


# In[19]:


cars.head()


# ## part 2:
# ## 8- make a subset of the data that has the car name, the price and name the new sub-setted data frame  car pricing.

# In[20]:


cars_pricing= cars[['car_name','Price']]


# In[21]:


cars_pricing


# ## 9- create a function called pricing category that returns "Budget Car " if the cars are less than 20,000 USD," Suitable Car " is the car is more than 20,000 and less than 35 000 and finally an expensive car for cars more than 35000.

# In[22]:


def pricing_category(price):
    if( price < 20000):
        a= 'Budget Car'
    if((price>= 20000)&(price<= 35000)):
        a= 'Suitable Car'
    if(price >35000):
        a= 'Expensive Car'
    return a


# In[23]:


pricing_category(50000)


# In[24]:


def pricing_cat(price):
    if price < 20000:
        return 'Budget Car'
    elif 20000 <= price <= 35000:
        return 'Suitable Car'
    else:
        return 'Expensive Car'


# In[25]:


pricing_cat(10000)


# ## 10- create a column named category on the subset using a for loop and pricing category function

# In[27]:


cars_pricing['category']


# In[28]:


cars_pricing.head()


# In[29]:


for i in range(cars_pricing.shape[0]):
    cars_pricing.category[i]= pricing_category(cars_pricing.Price[i])


# In[30]:


cars_pricing


# ## 11- How many Budget cars, suitable cars, and expensive cars we have?

# In[31]:


cars_pricing.category.value_counts()

