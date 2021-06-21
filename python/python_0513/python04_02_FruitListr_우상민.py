
cnt = []
fruitCnt = [] # 과일 카운트 리스트
fruit = ['Apple', 'Melon', 'Grape', 'StrawBerry']

while True:
    n = int(input("10이상의 수를 입력해주세요: "))
    if n >= 10:
        print("==<< %d번 반복합니다. >>==" % n)
        for i in range(1,n+1):
            if i % 3 == 0:
                cnt.append("Apple")
            if i % 4 == 0:
                cnt.append("Melon")
            if i % 5 == 0:
                cnt.append("Grape")
            if i % 8 == 0:
                cnt.append("StrawBerry")
            fruitCnt += cnt

            if len(cnt) == 0:
                print("%d. " % i)
            else:
                print("%d. " % i, str(cnt))
            cnt = []

        print("==<< Fruit Counter List >>==")
        for i in range(len(fruit)):
            print(fruit[i], ": %d회" % fruitCnt.count(fruit[i]))
    else:
        if n == 0:
            print("종료합니다.")
            break
        else:
            print("10이상의 숫자를 입력하세요!")