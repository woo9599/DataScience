
# coding: utf-8

# In[5]:


import pandas 


# In[30]:


import pandas as pd
#read_csv_sample.csv
#pd.read_csv
file_path =".\\dataSet\\read_csv_sample.csv" # .\\ 현재폴더 ..\\ 이전폴더 # \\ 경로 설정시 2개 \ 한개쓰면 한개로인식
df = pandas.read_csv(file_path)
print(df)
print (type(df))
a ='tr'
print (type(a))

