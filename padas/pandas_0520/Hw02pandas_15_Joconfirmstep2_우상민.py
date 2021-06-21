'''
조건 
- 4인 이상이 들어오면 len() 인원수 반환
- 인원수 반환 받으면 5명이면 -> 1~5
- 중복없이 반환

sample run]

보라돌이 뽀오 나나 뚜비 
4             1      2      3
'''
'''
for idx in range(5):
	print("%d"%random.randint(1,5),end='')
	for idx in range(idx-1):
		if(idx-1
	list01 = [4,4_

'''
import sys
import random

while True:
	a= []

	a = input("4인 이상의 이름을 입력하세요.(종료 : 0):").split()
	if '0' in a:
		exit()
	
	if len(a)<4:
		print("^\t명수를확인하세요.")
		continue
	else:
		while True:
			num = random.randint(1,len(a))
			if num not in b:
				b.append(num)
			else:
				continue

			if len(b) == len(a):
				break
		for i in a:
			print(i, end='')
		print('이고')
		for i in b:
			print(i,end='')
		print("입력되었습니다.")