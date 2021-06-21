
# coding: utf-8

# In[2]:


#**딕셔너리로 만들어져서 출력
#key = value 형태의 결괏값이 그 딕셔너리에 저장된다

def print_Kwargs(**Kwargs):
    print(Kwargs)
    
print_Kwargs(a=1)
print_Kwargs(name='foo',age =3)

