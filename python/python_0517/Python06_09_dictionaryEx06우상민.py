#Python06_09_dictionaryEx06우상민.py

#key로 value 얻기(get)
a = {'name':'pey','phone':'011999323','birth':'1118'}
print(a.get('name'))
print('-'*15)

'''
get(x) 함수는 x라는 key에 대응 되는 value를 들려준다.
a['nokey']는 key 오류를 발생시키고 a.get('nokye')는 None을
들려준다는 차이가 있다.
'''

print(a.get('mokey'))
#print(a['nokey'])

print('-'*15)