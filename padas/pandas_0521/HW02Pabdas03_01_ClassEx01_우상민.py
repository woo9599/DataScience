
# coding: utf-8

# In[3]:


'''
클래스: 재사용 : 틀 , 구조 : (함수 + 속성(변수)) class (Fourcal):(생성구조)
객체: 클래스로 부터 생성 
생성자 : 함수,클래스 이름과 동일한 함수, 주로 초기화에 사용

Ex)- 거푸집: 클래스 
-거푸집으로 부터 생성된 것: 객체 
- 풀빵틀 : 클래스
- 풀빵: 객체

## 클래스 사용
- 객체 생성후 사용
- 객체.속성, 객체.함수....
'''

class Fourcla:
    def setdata(self,first,second):
        self.first = first    #self(객체).first = 속성
        self.second = second

a = Fourcla() # a= 객체, Fiurcal= 생성자
a.setdata(4,2)

print(a.first)
print(a.second)
print(type(a))

