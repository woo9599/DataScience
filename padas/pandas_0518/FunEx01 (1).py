
# coding: utf-8

# ### 기본 함수 선언연습 01
# <h1> 기본 연습</n1> 
# <h2> 기본 연습</n2> 
# <h3> 기본 연습</n3> 
# <h4> 기본 연습</n4> 
# <h5> 기본 연습</n5> 
# HTML : Hyper Text Markup Langugg
# 

# In[22]:


def add(a,b):  #a,b는 매개 변수
    return 3 

a=3
b=4
c=add(a,b)     #3,4는 인수

print("%d + %d = : %d"%(a,b,c))


# In[9]:


#매개변수 지정하여 호출하기
#1.일반적인 함수

def add(a,b): # a,b는 매개변수
    return a,b,a+b
a,b,result = add(b=5,a=3)
print("%d + %d = %d" %(b,a,result))
print('-'*20)


# In[11]:


#2.입력값이 없는 함수
def say():
    return'hi'
print(say())
print("-"*20)


# In[13]:


#3.결괏값이 없는 함수
#결괏값은 오직 return 명령어로만 돌려 받을수 있다.

def add2(a,b):
    print("%d,%d의 합은 %d입니다."%(a,b,a+b))

print(add2(3,4))
print("-"*20)


# In[15]:


#4.입력값도 결괏값도 없는 함수

def say2():
    print('hi')
    
say2()
print("-"*20)

