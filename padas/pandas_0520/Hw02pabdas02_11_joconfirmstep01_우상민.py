#Hw02pabdas02_11_joconfirmstep01_우상민
'''
input 함수 이용
결과 : 4인 이상의 이름을 입력하세요...(sb로 구분한다.):보라돌이 나나 
- 4인이 아니면 == > ^ 명수를 확인 하세요 (4인 이상)
- 만약 4인 이상이라면 ===> 입력된 이름을 넣어 주면 됩니다. 보라돌이 나나 뚜비 뽀오 입력되었습니다.
'''

#a = input('4인이상의 이름을 입력하세요:').split(' ')

'''
print(" ".join(a))

if len(a) >= 4:
	print(" ".join(a),'입력되었습니다.')
else:
	print('명수를 확인하세요')
'''	


while True:
	a=[]
	a = input('4인이상의 이름을 입력하세요:').split(' ')

		if:
			for i in a:
				print('%d가 입력되었습니다.'%i)
		else:
			len(a) < 4:
			print('명수를확인하세요')
			continue
			

	
