
# coding: utf-8

# In[8]:


import pandas as pd
#sheet_name ='시트1'
#header =None.
df1 =pd.read_excel('./dataSet/datalabPractice01.xlsx')
df2 =pd.read_excel('./dataSet/datalabPractice01.xlsx',                   sheet_name ="Sheet1",usecols=[0,1,2],skiprows=[0],                   skipfooter=2,header =None)
#usecols=[0,1,2], skiprows=[1], skipfooter=1
#print(df1,iloc[[0,2],[1,2]],"\n")


print(df2.columns,"\n")
print(df2,"\n")
print(df1)

