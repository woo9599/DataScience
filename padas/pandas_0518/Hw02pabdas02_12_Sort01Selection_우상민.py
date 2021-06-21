#Hw02pabdas02_12_Sort01Selection_우상민

'''
selection sort
1. 오름 차순
      숫자 : 작수 ---> 큰수
	  영문 : a ----> z
	  한글 : ㄱ ----ㅎ

2. 내림차순
        숫자: 큰수 ---> 작수
		영문: z ---->A
		한글 : ㅎ --->ㄱ
'''
'''
outer
- idx :0, len-1

inner
-idx :1 ,len
'''
'''
sortNum = [2,5,6,1,2,8,33,77,12]
#결과값 = 1,2,2,5,6,8,12,33,77
print(sortNum)
'''

'''
for idx in range(len(sortNum)-1):
	for idx2 in range(idx+1,len(sortNum)):
		if(sortNum[idx] > sortNum[idx2]):
			print(sortNum[idx],sortNum[idx2])
'''
		

a= [2,5,6,1,2,8,33,77,12]

for i in range(len(a)-1):
	for j in range(i+1,len(a)):
		if a[i] > a[j]:
#			a[i], a[j] = a[j], a[i]
			tmp = a[i] #a[i] 값과 a[j]값을 바꾸기 위해tmp 사용
			a[i] = a[j]
			a[j] = tmp

for i in a:
	print(i, end=' ')



'''
i -0
j-1
'''




'''
a = [2,5,6,1,2,8,33,77,12]
#a.sort
#print(a)
for i in range(len(a)):
	print(i.sort())
	
'''

	

