##python02_07_autoMachine_우상민.py

print("*" *10 , '홍익대학교과일판매머신vo1', "*" *10)

print("1. orange : 1000원")

print("2. strawberry  : 2500원")

print("3. peach : 1500원")

print("4. mango : 2000원")

print("5. grape : 2000원")

print("종료")


print("="* 50)



while True:
	a = int(input("구매번호를 입력하세요. :"))
	if a == 1:
		print("oreange 1000원 입니다.")
	elif a == 2:
		print("strawberry 2500원 입니다.")
    elif a == 3:
		print("peach 1500원 입니다.")
    elif a == 4:
		print("mango 2000원 입니다.")
    elif a == 5:
		print("greape 2000원 입니다.")
    elif a == 6:
		print("종료")
	break


 
