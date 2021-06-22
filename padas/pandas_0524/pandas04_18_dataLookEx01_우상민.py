
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./data/gapminder.tsv', sep='\t')


# In[3]:


print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[4]:


len(df)


# In[5]:


df[0:5]


# In[6]:


df.head(n=7)


# In[7]:


df.tail()


# In[8]:


df[len(df)-5:len(df)+1] # tail 값이랑 똑같음 


# In[9]:


df.tail(n=7)


# In[10]:


#데이터의 자료형을 확인
type(df)


# In[11]:


#데이터프레임의 열 확인
print(df.columns)


# In[12]:


#데이터프레임의 행확인
df.index


# In[13]:


#데이터프레임을 구성하는 값의 자료형을 확인
print(df.dtypes)


# In[14]:


#데이터집합과 각열들의 자료형을 자세히 확인
print(df.info())


# In[15]:


#에서는 (행,열)크기를 알수 있습니다.
df.shape


# In[16]:


#데이터집합과 각 열들의 자료형을 자세히 확인
print(df.info())

