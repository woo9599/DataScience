#Python06_12_studentMS_step02List_우상민.py
# dic['key값'] = value
#------------
#1.문제)dic 에 idList를 key값으로 하고, scoreList를 value값으로 할당
#dic['idList'] = scoreList
#------------

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;
s=0;

def inputData():
    for i in range(len(idList)):
        dic[idList[i]] = scoreList[i]
    
def PrintList():
	s=0
	for i in range(len(MenuList)):
		print(MenuList[i],end='     ')
	print('')
	for i in dic:
		print(i, end ='\t')
		for j in range(len(dic[i])):
			 print(dic[i][j],end='\t')
			 s =dic[i][j] +s		 
		print('%d \t %0.0f'%(s,s/len(dic[i])), end ='\t')
		if s/len(dic[i]) >= 70:
			print('합격')
		else:
			print('불합격')
		s=0	 
		print('')
	print('\n',"-"*60)

def DelId():
	a = input("1.회원 탈퇴 아이디를 입력하세요:")
	if a in idList:
		del dic[a]
		deleteIDList.append(a)
		print(a)

def SignIn():
	score=[]
	newID = input("2. 회원을 추가 등록하세요:") 
	if newID in deleteIDList:
		print("탈퇴된아이디입니다.")
	elif newID in dic.keys() :
		print("중복된 아이디 입니다.")
	else:
		for i in range(1,len(itemList)):
			score.append(int(input('%s'%itemList[i])))# 실기 점수, 인성점수,필기점수
		dic[newID] = score


def passStudent():
	for i in dic.keys():
		s=0
		for j in range(len(dic[i])):
			s =dic[i][j]+s
		if s/len(dic[i]) >= 70:
			print(i)
			




	    

	

      
	

def Mainpg():
	menu = int(input('번호입력:'))
	if menu == 1:
		DelId()
	elif menu== 2:
		SignIn()
	elif menu == 3:
		print("3.학생목록:")
		PrintList()
	elif menu == 4:
		print("4.합격생목록:")
		passStudent()
	elif menu ==9:
		print("9.메뉴종료.")
		exit() # exit 파이썬 종료 함수 return 0 함수를 종료 해주는 것
	else:
		print("다른번호입니다.")



print('-'* 60)
print("학생관리시스템v10")
print('-'* 60)
#print('1. 탈퇴학생', '2. 추가등록', '3.학생목록','4.합격생목록','9메뉴종료')
for i in range(len(menu)):
	print(menu[i], end='')
print('\n','-'* 60)

inputData()
while True:
	Mainpg()
	'''
	menu = int(input('번호입력:'))
	if menu == 1:
		DelId()
	elif menu== 2:
		SignIn()
	elif menu == 3:
		print("3.학생목록:")
		PrintList()
	elif menu == 4:
		print("4.합격생목록:")
	elif menu ==9:
		print("9.메뉴종료.")
		break
	else:
		print("다른번호입니다.")
'''	
