#Python06_07_dictionaryEx04_우상민.py

'''
딕셔너리 관련 함수들
key 리스트 만들기(keys)
'''

a= {'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())
'''
dict_keys,dict_values,dict_items 등은 리스트로 변환하지 않더라도
기본적인 반복 구문을 실행할수있다.
'''

for k in a.keys():
	print(k)


print('-'*15)

#dic_keys 객체를리스트로 변환하려면 다음과 같이 하면 된다.
vList = list(a.keys())
print(vList)
print('-'*15)

