
# coding: utf-8

# In[1]:


'''
전역 변수 : 함수 외에 선언 하는 것
              - 모든 함수 공유

지역 변수 : 함수 내에 선언 하는 것
              - 함수와 생명력을 같이 한다.(매개 변수도 지역변수)

함수 안에서 선언한 변수의 효력 범위
함수 안에서 사용하는 매개변수는 지역변수이다.

함수 안에서 함수 밖의 변수를 변경하는방법

'''

a=1
def vartest(a):
    a= a+1
    print(a)

vartest(a)

print(a)
print('-'*20)

