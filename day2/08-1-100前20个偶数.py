i = 1
num = 0
while i <= 100 :
	#if i 是个偶数 就打印
	if i%2 == 0:
		print(i)
		num += 1
	
	
	
	if num == 20:
		break
	i += 1


print('-'*50)

print(num)
print(i)
