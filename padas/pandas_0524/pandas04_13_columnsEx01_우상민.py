
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./data/gapminder.tsv', sep='\t') #(열,행)
df.shape


# In[3]:


df.columns # 안에 속성을 보여준다.

