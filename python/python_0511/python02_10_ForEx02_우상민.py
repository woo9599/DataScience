#python02_10_ForEx02_우상민

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
	number = number +1
	if mark >= 60:
		print(number, "번 학생은 합격입니다.")
	else:
		print(number,"번 학생은 불합격입니다.")