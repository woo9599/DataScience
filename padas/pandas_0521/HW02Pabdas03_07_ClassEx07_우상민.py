
# coding: utf-8

# In[1]:


class FourCal:
    def __init__(self,first,second): #__ 생성자 
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
    
class SafeFourCal(FourCal): # fourcal 상속 받음
    def div(self): #현재 매소드 
        if self.second ==0:
            return 0
        else:
            return super().div() # 상위 (Fourcal값을 가져오겠다)

a = SafeFourCal(4,0)

print(a.first,"+",a.second, "=",a.sum())
print(a.first,"-",a.second, "=",a.sub())
print(a.first,"*",a.second, "=",a.mul())
print(a.first,"/",a.second, "=",a.div())

