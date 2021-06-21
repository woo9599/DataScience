
# coding: utf-8

# In[1]:


'''
override
-상속 받은 곳에서 부모 메소드 재정의
- 현재 메소드 무산
'''
class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def sum(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first -self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
class SafeFourCal(FourCal):
    def div(self): #현재 매소드
        if self.second ==0:
            return 0

a = SafeFourCal(4,0)

print(a.first,"+",a.second, "=",a.sum())
print(a.first,"-",a.second, "=",a.sub())
print(a.first,"*",a.second, "=",a.mul())
print(a.first,"/",a.second, "=",a.div())

