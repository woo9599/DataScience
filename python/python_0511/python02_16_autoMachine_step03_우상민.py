#python02_16_autoMachine_step03_우상민

menu = ['오렌지', '딸기', '복숭아','망고','포도','종료']
money = [1000, 2500, 1500,2000,2000]

print("*" *10 , '홍익대학교과일판매머신vo1', "*" *10)

for i in range(0,5):
	print(i+1,"번",menu[i],":", menu[i],"원")
print("6.종료")
print("="*50)

print("="* 50)

while True:
	num = int(input("구매번호를 입력하세요: "))

	if num ==1:
		print(menu[num-1], "는", money[num-1],"원 입니다.!")
		print("<" * 30)

	elif num ==2:
		print(menu[num-1], "는", money[num-1],"원 입니다.!")
		print("<" * 30)
	elif num ==3:
		print(menu[num-1], "는", money[num-1],"원 입니다.!")
		print("<" * 30)

	elif num == 4:
		print(menu[num-1], "는", money[num-1],"원 입니다.!")
		print("<" * 30)

	elif num == 5:
		print(menu[num-1], "는", money[num-1],"원 입니다.!")
		print("<" * 30)

	elif num == 6:
		print("6.exit")
		break

	else:

		print("없는 메뉴 입니다.!")
		print("<" * 30)
