
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({'float': [1.0],'int':[1],                   'datetime':[pd.Timestamp('20180301')],                  'string':['foo']})


# In[3]:


print(df)
df.dtypes

