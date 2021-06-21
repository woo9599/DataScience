##python05_01_fruitliststep01_우상민


a = 0
b = 0
s = 0
g = 0

while True: ##
	num = int(input('10이상의 수를 입력하세요.[exit: 0 ] >>>>'))
	if num >= 10:
		print("FruitList Algorithm chk")
	elif(num == 0):
		print("^종료!!")
		break
	else:
		print("^ 10이상의 숫자를 확인하세요.")
		continue