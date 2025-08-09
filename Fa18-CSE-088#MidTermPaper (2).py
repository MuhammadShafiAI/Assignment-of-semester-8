#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import seaborn as sns


# In[64]:


import matplotlib.pyplot as plt


# In[66]:


data =pd.read_csv('titanic.csv')


# In[67]:


X = data.iloc[:,0:20]


# In[68]:


y = data.iloc[:,-1]


# In[69]:


correlation_matrix = data.corr()


# In[70]:


top_corr_features = correlation_matrix.index


# In[71]:


plt.figure(figsize=(20,20))


# In[74]:


g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")


# In[ ]:


#Here all the value with color of red which are (-0.34 and -0.55 ) are negatively correlated means perfect inverse correlated
#All the values in light yellow are zero(0) are called no correlated values and there is no correlation relationship with output.
#All the values in green are perfect direct correlation which is (1) and direct correlation with  output variable
#All the values between (0.2 to 1 ) are positvely correlated and and direct correlation with output

