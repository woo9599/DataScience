
# coding: utf-8

# In[9]:


'''
a.first + a.second = a.sum
'''


class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second =second
        
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
        
a =FourCal()#객체생성
a.setdata(4,2)

print(a.sum())
    
    

