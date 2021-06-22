
# coding: utf-8

# In[1]:


import pandas as pd

#HTML 파일경로 or 웹페이지 주소를 url 변수에 저장

url = './DataSet/htmltest.html'

# HTML 웹페이지의 표를 가져와 데이터프레임으로 변환
tables = pd.read_html(url)

#표의 개수 확인
print(len(tables), '\n==>')

print(tables,'\n==>')

#테이블 리스트의 원소를 teration하면서 각각 화면 출력

for i in range(len(tables)):
    print("tables[%s]"%i,'\n')
    print(tables[i],'\n')
    
#파이썬 패키지 정보가 들어 있는 두번째 데이터프레임을 선택하여 df변수에저장

df = tables[1]
print(df.columns,'\n')

