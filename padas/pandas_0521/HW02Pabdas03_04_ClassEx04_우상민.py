
# coding: utf-8

# In[20]:



'''
오버라이드 : 상속도 재사용 
생성자에서 초기화 할수 있어요
'''

class FourCal:
    def __init__ (self):  # 기본 생성자 
        pass  # 아무것도 없을 때 pass사용
    def __init__(self,first,second):
        self.first = first #매개변수2개 생성자 생성 
        self.second=second#@오버로드 같은 클래스 같은 메소드 1개 이상(이름이 똑같으면 매개변수갯수로 구분)
        
    def sum(self):
        result = self.first+self.second
        return result
    
    def sub(self):
        result= self.first-self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first/self.second
        return result
    
    
#a = FourCal()
#a.setdata(4,2)
        
a = FourCal(4,2)
print(a.sum())

