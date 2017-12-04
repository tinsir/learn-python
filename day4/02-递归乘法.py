def chengfa(num):
	if num > 1:
		return num * chengfa(num - 1)
	else:
		return num

result = chengfa(4)

print(result)
