##python05_03_fruitlistsample02_우상민.py

N = int(input('Input :'))
fruitList = ["Apple", "Melon","Grape","strawBertty"]
fruitNumber = [3,4,5,8]
fruitCount = [0,0,0,0]

print("== << %d회 반복 합니다. >> =="%N)
for i in range(1, N+1):
	print("\n%2d." %i, end="")
	for j in range(len(fruitList)):
		if(i % fruitNumber[j] == 0):
			fruitCount[j] += 1
			print("%s" % fruitList[j], end = " ")


print("\n\n == << Fruit count List >> ==")
for i in range(len(fruitList)):
	print("%d. %-12s %2d회" % (i +1, fruitList[i], fruitCount[i]))