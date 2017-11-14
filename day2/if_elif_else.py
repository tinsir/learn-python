money = int(input('请输入你的金额'))

if money < 100:
	#一些便宜的水果
	print('cheap fruits')
elif money == 100:
	#相当的水果
	print('quite fruits')
elif money > 100 and money < 200:
	#很多的水果
	print('a lot of fruits')
else:
	print('whatever')
