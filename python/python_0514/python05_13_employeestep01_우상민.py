##python05_13_employeestep01_우상민.py
# 인사관리 시스템
#사번,이름,입사일,급여
#사번 1번째
#T,t<<계약직
#R << 정규직


TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],
    ['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]


'''
if empInfo[1][0][0] == 't' or empInfo[1][0][0] == 'T':
	del empInfo[1][0]
	empInfo[1].insert(0,"계약직")
elif empInfo[1][0][0] == 'r' or empInfo[1][0][0] == 'R':
	del empInfo[1][0]
	empInfo[1].insert(0, "정규직")

print(empInfo[1])

'''


for i in range(len(empInfo)):
	print("%s	%s	%s	"%(empInfo[i][0][0],empInfo[i][1],empInfo[i][2]))
	if empInfo[0][0][0] == 't' or empInfo[0][0][0] == 'T':
		del empInfo[0][0]
		empInfo[0].insert(0,"계약직")
	elif empInfo[0][0][0] == 'r' or empInfo[0][0][0] == 'R':
		del empInfo[1][0]
		empInfo[1].insert(0,"계약직")
		
		empInfo[i].append(empTable[i])


print("구분\t사원명\t입사일\t\t급여")
print("-"*40)
for i in range(len(empInfo)):
	print("{0:}\t{1:}\t{2:}\t{3:,d}".format(empInfo[i][0],empInfo[i][1],empInfo[i][2],empInfo[i][3]))
	print("-"*40)


'''


''
print("계약직\t캔디\t2016 - 05 - 10" "2500")
print("정규직\t캔디\t2016 - 05 - 10" "2500")
print("계약직\t캔디\t2016 - 05 - 10" "2500")
print("계약직\t캔디" "2016 - 05 - 10" "2500")
print("정규직\t캔디" "2016 - 05 - 10" "2500")
'''


#print(TName)


#for i in range

#result = empInfo.pop()
#print 
#while empInfo:
	#pop()
	
#print(str(empInfo.index(T,t)))
#print(str(empInfo.find(T,t))
#print(empInfo.list())
#print("-" * 40)
#print(empInfo.index(T))
#print(empInfo.index(T,t))

