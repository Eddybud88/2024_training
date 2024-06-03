# 3.1 
# 列表创建
games = ['Resident Evil' , 'The Wicher 3' , 'GTAV' , ' Assassin Creeds']
print(games)

['Resident Evil', 'The Wicher 3', 'GTAV', ' Assassin Creeds']

# 访问列表元素
games = ['Resident Evil' , 'The Wicher 3' , 'GTAV' , ' Assassin Creeds']
print(bicycles[2]) #注意从0开始

GTAV

# 使用列表中的值
games = ['Resident Evil' , 'The Wicher 3' , 'GTAV' , ' Assassin Creeds']
message = "My favourite game is " + games[2] + "."
print(message)

My favourite game is GTAV.

#3.2 修改、添加和删除元素
# 修改元素
F1  =  ['Ferrari',  'McLaren',  'Red Bull'] 
print(F1)
F1[2]  =  'Alpine' 
print(F1)

['Ferrari', 'McLaren', 'Red Bull']
['Ferrari', 'McLaren', 'Alpine']

# 添加
F1  =  ['Ferrari',  'McLaren',  'Red Bull'] 
F1.append('Aston Martin') 
print(F1)

['Ferrari', 'McLaren', 'Alpine', 'Aston Martin']

# 插入
F1  =  ['Ferrari',  'McLaren',  'Red Bull'] 
F1.insert(0,  'Hass') 
print(F1)

['Hass', 'Ferrari', 'McLaren', 'Red Bull']

# 删除
# 已知位置
F1  =  ['Ferrari',  'McLaren',  'Red Bull'] 
del F1[2]
print(F1)

['Ferrari', 'McLaren']

# 删除并继续使用
F1  =  ['Ferrari',  'McLaren',  'Red Bull'] 
pop_F1 = F1.pop(2)
print(F1)
print(pop_F1)

['Ferrari', 'McLaren']
Red Bull

# 位置未知
F1  =  ['Ferrari',  'McLaren',  'Red Bull' , 'Aston Martin'] 
F1.remove('Red Bull')
print(F1)

['Ferrari', 'McLaren', 'Aston Martin']

#3.3 组织列表
# 永久性与临时排序
F1  =  ['Ferrari',  'McLaren',  'Red Bull' , 'Aston Martin'] 
F1.sort() #永久
print(F1)

['Aston Martin', 'Ferrari', 'McLaren', 'Red Bull']


F1  =  ['Ferrari',  'McLaren',  'Red Bull' , 'Aston Martin'] 
print(sorted(F1))  #临时
print(F1)

['Aston Martin', 'Ferrari', 'McLaren', 'Red Bull']
['Ferrari', 'McLaren', 'Red Bull', 'Aston Martin']

# 反转
F1  =  ['Ferrari',  'McLaren',  'Red Bull' , 'Aston Martin'] 
F1.reverse()
print(F1)

['Aston Martin', 'Red Bull', 'McLaren', 'Ferrari']

# 求长度
F1  =  ['Ferrari',  'McLaren',  'Red Bull' , 'Aston Martin']
len(F1)

4

