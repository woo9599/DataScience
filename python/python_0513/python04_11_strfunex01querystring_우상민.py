#python04_11_strfunex01querystring_우상민.py

str1= 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python\n\n'.split('?')
str2= str1[1]
strr= str2.split('&')
print('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python\n\n')
print("URL\nQueryString\n")
for i in range(len(strr)):
	print("\t",strr[i])
print("QueryString 개수 : %d개\n" % len(strr))