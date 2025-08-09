#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[37]:


data = pd.read_csv("titanic.csv")
data


# In[38]:


x = data.iloc[:,0:12]
y = data.iloc[:,-1]
x


# In[44]:


y


# In[49]:


correlation_matrix = data.corr()
correlation_matrix


# In[50]:


top_correlation_features = correlation_matrix.index
top_correlation_features


# In[47]:


plt.figure(figsize=(20,20))


# In[51]:


g=sns.heatmap(data[top_correlation_features].corr(),annot=True,cmap="RdYlGn")
# corelation between passengerid and survived is -ve. while corelation between passengerid and fare is +ve
# while correlation between age and parch is -0.19 which is -ve. Correlation between age and fare is 0.096 which is positive


# In[ ]:




