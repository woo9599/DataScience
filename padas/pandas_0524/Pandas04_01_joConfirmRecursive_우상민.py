

import random

lst =[]

def recursive(m):# 재귀함수를 받는 구간 
	if(chk == len(lst)):
		return
	
	for i in range(m):
		num = random.randint(1,len(name))
		if num not in lst:
			lst.append(num)
		else:
			recursive(chk-len(lst)) # 재귀함수 

while True:
	name = input("4인 이상의 이름을 입력하세요.").split(' ')
	if len(name)>=4:
		for i in name:
			print(i,end=' ')
		print('')

		chk = len(name)

		lst =[]
		cnt =0

		recursive(chk) # 첫번째 호출을 
		print(lst)