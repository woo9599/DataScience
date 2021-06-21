print("1단  2단  3단  4단  5단  6단  7단  8단  9단")
print('-'*60)

for i in range(2,10):
	for j in range(1,10):
		print("%d X %d = %d"%(j,i,j*i),end='	')
	print()