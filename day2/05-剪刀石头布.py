import random

player = int(input('请输入序号 剪刀:0 石头:1 布:2'))

computer = random.randint(0,2)

#print(computer)

#判断赢的条件

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
	print('YOU WIN')
#判断输的条件

if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
	print('YOU LOST')
#判断平的条件

if (player == computer):
	print('平局')
