
# coding: utf-8

# In[5]:


import pandas 


# In[32]:


import pandas as pd
#read_csv_sample.csv
#pd.read_csv
file_path =".\\dataSet\\read_csv_sample.csv" # .\\ 현재폴더 ..\\ 이전폴더 # \\ 경로 설정시 2개 \ 한개쓰면 한개로인식
df = pandas.read_csv(file_path)
print(df)
print (type(df))
a ='tr'
print (type(a))


# In[34]:


#read_csv() 함수로 데이터프레임 변환.변수 df2에 저장.header=None옵션
df2 = pd.read_csv(file_path, header=None)
print(df2,'\n')

#read_csv() 함수로 데이터프레임 변환.변수 df3에 저장. index_col=None옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3,'\n')
#read_csv() 함수로 데이터프레임 변환.변수df4에 저장.index_col='c0'옵션
df4 =pd.read_csv(file_path, index_col='c0')
print(df4)

