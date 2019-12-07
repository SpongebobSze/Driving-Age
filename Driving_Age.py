# 驾驶年龄限制
Country = input('你来自哪个国家: ')
if Country == '台湾':
	print('甘霖娘，台湾是中国的一个省！')
elif Country == '中国':	
	Age = input('请输入年龄: ')
	Age = int(Age)
	if Age >= 18:
		print('可以考驾照啦')
	else:
		print('滚')
elif Country == '美国':
	Age = input('请输入年龄: ')
	Age = int(Age)
	if Age >= 16:
		print('可以考驾照啦')
	else:
		print('滚') 
else:
	print('其他国家我管不了')