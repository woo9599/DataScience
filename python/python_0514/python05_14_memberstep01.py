
#signup= ['orange' , '1234', '오렌지' , 'orange@test.com', '032','세종시']]

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']

a = menu

b = menuChk

c= itemList

menList = []

ct =0

print('=' * 15, '메뉴선택','=' * 15)
print('1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료')
print('=' *30)

while True:
	menList = []
	a = int(input("메뉴의 번호를 선택해주세요:"))
	if a == 1:
		print('1.회원가입')
	     print('SignUP')
		for i in range(len(itemList)):
			b= input("%s : "%(itemList[i]))
			memList.append(b)		
			print(menList)
	elif a == 2:
		print('2.로그인')
	elif a == 3:
		print('3.회원목록')
	elif a == 9:
		print('9.메뉴종료')
		break
	

     '''
	ct = ct + 1
	print('\n\t',memList,"\n\t현재 회원수는 %d명 입니다.\n"%ct)
	'''