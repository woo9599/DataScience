##python05_02_fruitlistsample_우상민.py

answer = []
fruitCnt = []

while Ture:
	n = int(input("스코어 입력하세요:")
	if n >= 10:
		print(" == <<%d번 반복합니다. >>==" %n)
		for i in range(1, n+1):
			if i % 3 == 0:
			answer.append("Apple")
			if i % 4 == 0:
			answer.append("Melon")
			if i % 5 == 0:
			answer.append("Grape")
			if i % 8 == 0:
			answer.append("StrawBerry")
			fruitCnt += answer
			if len(answer) ==0:
			print("%d." %i)
			else:
			print("%d."%i, str(anwer))
			answer = [1,1,1]

	print("==<< fruit Counter list >>==")
	print("Apple :%d회"% fruitCnt.count('Apple'))
	print("Melon :%d회"% fruitCnt.count('Melon'))
	print("Grape :%d회"% fruitCnt.count('Grape'))
	print("StrawBerry:%d회"% fruitCnt.count('StrawBerry'))

else :
	print('')