
# coding: utf-8

# In[2]:


'''
매개변수에 초깃값 미리 설정하기
say_myself함수는 3개의 매개변수를 받아서 마지막 인수인
man이 true이면"남자입니다",false이면"여자입니다"를 출력
'''

def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다."%name)
    print("나이는%d살입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다")
        
say_myself("소나무",27)
print("-"*20)
say_myself("오렌지",25,False)
print("-"*20)

