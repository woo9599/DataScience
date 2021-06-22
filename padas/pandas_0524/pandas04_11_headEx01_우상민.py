
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


df = pd.DataFrame({'animal' : ['alligator','bee','falcon','lion','monkey','parrot','shark','whale','zebra']})


# In[14]:


print(df)


# In[15]:


print(df.head()) # 5개 출력


# In[16]:


print(df.head(3)) #앞에 3개 출력


# In[17]:


print(df.head(-3))# 뒤에 -3 빼고 나머지 출력

