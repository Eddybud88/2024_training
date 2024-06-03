names = ['Napolean' , 'Stalin' , 'Lennon']
names[1] = 'Judy Foster'
names.insert(0,  'Paul') 
names.insert(3, 'Ringo')
names.append('George')
print("But I can only invite 2 of U")
pop_name0 = names.pop(0)
print("Dear " + pop_name0 + " I'm sorry")
pop_name0 = names.pop(0)
print("Dear " + pop_name0 + " I'm sorry")
pop_name0 = names.pop(0)
print("Dear " + pop_name0 + " I'm sorry")
pop_name0 = names.pop(0)
print("Dear " + pop_name0 + " I'm sorry")
print("Dear " + names[0] + " you're still in the list")
print("Dear " + names[1] + " you're still in the list")
del names[0]
del names[0]
print(names)

输出：
But I can only invite 2 of U
Dear Paul I'm sorry
Dear Napolean I'm sorry
Dear Judy Foster I'm sorry
Dear Ringo I'm sorry
Dear Lennon you're still in the list
Dear George you're still in the list
[]
