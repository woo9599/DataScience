'''
가위 바위 보
가위가 1   딕셔너리 숫자가 키값으로 오게
바위가 2  딕셔너리  숫자가 키값으로 오게
보가 3     딕셔너리  숫자가 키값으로 오게
컴퓨터는 랜덤으로 3개를 받아야됨 = 1,2,3
유저 = 1,2,3을 입력 해야된다.
4를 입력하면 횟수 입력
9를 입력하면 종료

무한반복문 : 한번 돌때마다 카운트 몇번 했는지도 입력 

컴퓨터가 이겼는지 유저가 이겼는지 카운트 하는것도 필요#이거 해야되고


그 외 수를 입력하면 잘못 입력 해야 된다.

예를 들어 컴퓨터가 바위를 내면 랜덤수로 2를 냈다.

if 2==2:
	print("비겼습니다.") 요룡느낌 

컴퓨터가 바위 2  유저가 가위 1 
바위 승 
if 컴퓨가 숫자가 > 유저숫자 보다 높으면:
	print("컴퓨터가 이겼습니다.")

컴퓨터가 바위 2 유저는 보 3
if 컴퓨터 숫자가 2 < 유저 숫자보다 작으면 
print('유저가 이겼습니다.')

예외 처리
컴퓨터가 1 이고 유저가 3일시 
print(" 당신이 이겼습니다.")

유저가 1이고 컴퓨터가 3일시
print('당신이 졌습니다.')

'''


#ScoreList =['1','2','3']
#RpcList =['가위','바위','보']

dic= {1:'가위',2:'바위',3:'보'}
count =0
winCnt =[0,0]
#print(dicr)



import random
while True:
	print("1. 가위"," 2.바위"," 3. 보"," 4.횟수 입력"," 9.종료")
	user1 = int(input('숫자를 입력하세요:'))
	#Computer= int(input('숫자를 입력하세요:'))
	Computer = random.randint(1,3)
	#print(Computer)

	if user1 in range(1,4):
		 if Computer == user1:
			 print('비겼습니다')
		 elif Computer ==3 and user1 == 1:
			 print('유저가 이겼습니다')
			 winCnt[1] += 1
		 elif Computer ==1 and user1 == 3:
			 print('컴퓨터가 이겼습니다.')
			 winCnt[0] += 1
		 elif Computer < user1:
			 print('당신이 이겼습니다')
			 winCnt[1] += 1
		 elif Computer >user1:
			 print('컴퓨터가 이겼습니다')
			 winCnt[0] += 1
		 count = count+1	

		 print('현재 스코어 {winCnt[0]} : {winCnt[1]} (컴퓨터: 유저) 입니다')

	else:
		if user1 == 9:
			print('종료합니다')
			break
		elif user1 ==4:
			print('횟수입력')
		else:
			print('다른번호입니다.')
		
		



		
	

	


	
	

