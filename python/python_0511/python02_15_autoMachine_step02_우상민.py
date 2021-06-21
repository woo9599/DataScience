
#python02_15_autoMachine_step02_우상민



menu = ['오렌지', '딸기', '복숭아','망고','포도','종료']

print("*" *10 , '홍익대학교과일판매머신vo1', "*" *10)

for num in range(0,6):
	print(num + 1 , menu[num])


print("="* 50)

while True:
	a = int(input("구매번호를 입력하세요: "))

	if a ==1:

		print("orange는 1000원 입니다.")
		print("<" * 30)

	elif a ==2:

		print("strawberry는 2500원 입니다.")
		print("<" * 30)
	elif a ==3:

		print("peach는 1500원 입니다.")
		print("<" * 30)

	elif a == 4:

		print("mango는 2000원 입니다.")
		print("<" * 30)

	elif a == 5:

		print("grape는 2000원 입니다.")
		print("<" * 30)

	elif a == 6:
		print("6.exit")
		break

	else:

		print("없는 메뉴 입니다.!")
		print("<" * 30)
