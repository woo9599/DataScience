
# coding: utf-8

# In[1]:


# lambda 활용법


x = lambda a : a +10
print(x(5))

x = lambda a,b : a*b
print(x(5,6))

def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a: a*n

mytripler = myfunc(3)
print(mytripler(11))










'''
def myfunc(n):
	return lambda a: a*n

mydoubler = myfunc(2)
print(mydounler(11))
'''