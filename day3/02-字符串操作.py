name = 'zhangsan'

#字符串.find()

#find查找正序 n
print(name.find('n'))
#rfind查找逆序 n
print(name.rfind('n'))
#find找不到
print(name.find('ddddd'))

#字符串.index('')

#正序index查找
print(name.index('n'))
#逆序index查找
print(name.rindex('n'))
#index找不到 直接报异常  
#print(name.index('xxxxxxxxxxxxxxxx'))


#字符串.count()  用来统计字符个数

print(name.count('n'))

#字符串.replace("原始字符","替换为字符",替换次数)
#默认所有都替换  第三个参数可以控制替换次数

print(name.replace('n','&&&&&&&&&&&&&&',1))

#字符串.split("")
#按照一定字符串切割
#split()空白参数可以去除空格和\t


print(name.split('a'))


#字符串首字母大写


print(name.capitalize())

#字符串中每个单词首字母大写

name_2 = 'zhangsan lisi wangwu'
print(name_2.title())






