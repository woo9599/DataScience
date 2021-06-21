#Python06_11_studentMS_step01_우상민.py
# dic['key값'] = value
#------------
#1.문제)dic 에 idList를 key값으로 하고, scoreList를 value값으로 할당
#
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

print('-'* 60)
print("학생관리시스템v10")
print('-'* 60)
#print('1. 탈퇴학생', '2. 추가등록', '3.학생목록','4.합격생목록','9메뉴종료')
for i in range(len(menu)):
	print(menu[i], end='')
print('\n','-'* 60)


while True:
	menu = int(input('번호입력:'))
	if menu == 1:
		print("1.학생탈퇴:")
	elif menu== 2:
		print("2.추가등록:")
	elif menu == 3:
		print("3.학생목록:")
		#------------
        #3번을선택한경우 dic의 값을 출력
        #
        #------------
	elif menu == 4:
		print("4.합격생목록:")
	elif menu ==9:
		print("9.메뉴종료.")
		break
	else:
		print("다른번호입니다.")
	

