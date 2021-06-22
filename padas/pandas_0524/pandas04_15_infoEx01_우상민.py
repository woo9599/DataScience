
# coding: utf-8

# In[6]:


import pandas as pd
int_values =[1,2,3,4,5]
text_values = ['alpha','beta','gamma','delta','epsilon']
float_values = [0.0,0.25,0.5,0.75,1.0]
df = pd.DataFrame({'int_col':int_values, 'text-col':text_values,                   'float_col':float_values})
df


# In[7]:


df.info(verbose=False)


# In[8]:


df.dtypes


# In[9]:


df.info()


# In[10]:


df.info(verbose=True)

