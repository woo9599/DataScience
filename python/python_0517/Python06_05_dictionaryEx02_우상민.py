#Python06_05_dictionaryEx02_우상민.py
'''
딕셔너리 쌍 추가하기
a[2] = 'b'와 같이 입력하면 딕셔너리 a에 key와 value가 각각
2와 'b'인 2:'b'라는 딕셔너리 쌍이 추가
'''

a ={1:'a'}
a[2] ='b'
print(a)

a['name'] ='pey'
print(a)
print("-"*15)

#딕셔너리 요소
del a[1]
print(a)
print("-"*15)