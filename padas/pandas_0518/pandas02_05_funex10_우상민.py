
# coding: utf-8

# In[4]:


#lambda

'''
lambda는 함수를 생성할때 사용하는 예약어로 def와 동일한역할을
한다. 보통 함수를 한줄로 간결하게 만들 때 사용한다.
우리말로는 "람다"라고 읽고 def를 사용해야 할정도로 복잡하지 않거나
def를 사용 할수 없는 곳에 주로 쓰인다.
'''

add = lambda a,b:a+b   #def add(a,b)
result = add(3,4)       #   return a+ b
print(result)


#lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

