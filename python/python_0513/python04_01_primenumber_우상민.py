#python04_01_primenumber_우상민.py
#a = int(input('숫자를 입력하세요:'))
#cnt = 0
#while number % number == 0:
while True:
    n = int(input("수를 입력해주세요: "))
    cnt = 0

    if n >= 20:
        for i in range(1, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    cnt += 1
            if i == 1:
                print("%d : 소수 X" % i)
            elif cnt == 0:
                print("%d : 소수 O" % i)
            else:
                print("%d : 소수 X" % i)
            cnt = 0
    else:
        if n == 0:
            print("종료합니다.")
            break
        else:
            print("20이상의 숫자를 입력하세요!")


#while numder >= 20:
	
#if number % number ==0:
#	print('소수0')
#else:
#	print('소수x')
#elif

