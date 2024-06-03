names = ['Napolean' , 'Stalin' , 'Lennon']
names[1] = 'Judy Foster'
print("I have found a larger table.")
names.insert(0,  'Paul') 
names.insert(3, 'Ringo')
names.append('George')
print("Dear " + names[0] + ", I would like to invite you to have dinner with me.")
print("Dear " + names[1] + ", I would like to invite you to have dinner with me.")
print("Dear " + names[2] + ", I would like to invite you to have dinner with me.")
print("Dear " + names[3] + ", I would like to invite you to have dinner with me.")
print("Dear " + names[4] + ", I would like to invite you to have dinner with me.")
print("Dear " + names[5] + ", I would like to invite you to have dinner with me.")

输出：
I have found a larger table.
Dear Paul, I would like to invite you to have dinner with me.
Dear Napolean, I would like to invite you to have dinner with me.
Dear Judy Foster, I would like to invite you to have dinner with me.
Dear Ringo, I would like to invite you to have dinner with me.
Dear Lennon, I would like to invite you to have dinner with me.
Dear George, I would like to invite you to have dinner with me.
