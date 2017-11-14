fruits = input('梨或者苹果')
money  = input('你有多少钱')
money  = int(money)
if fruits == '梨':
	print('梨好吃')
if money >= 100:
	print('你可以买很多梨')

print( "*" * 20) 
if fruits == '梨' and money >= 100 :
	print('很健康')

print( "0" * 20)
if fruits == '苹果' and money >= 100 :
	print('吃点梨也不错,钱足够')
