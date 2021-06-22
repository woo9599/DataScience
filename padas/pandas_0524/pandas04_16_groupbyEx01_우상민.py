
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


df = pd.DataFrame({'Animal':['Falcon','Falcon','Parrot','Parrot'],                   'Max Speed':[380.,370.,24.,26.]})
df


# In[6]:


df.groupby(['Animal']).mean()

