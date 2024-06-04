car = 'RR'
if car != 'Airbus':
  print("Not True")
plane = 'Airbus'
if plane == 'Airbus':
  print("Alright")
machine = 'Boeing'
print(machine == 'boeing')
print(machine.lower() == 'boeing')
age = 22
print(age == 22)
print(age != 22)
print(age <= 9)
print(age >= 25)
age1 = 23
age2 = 25
print(age1 == 22 and age2 == 22)
print(age1 == 23 or age2 ==23)
names = ['Napolean' , 'Stalin' , 'Lennon']
name1 = 'Lennon'
name2 = 'Lenin'
if name1 in names:
  print("Yeah!")
if name2 not in names:
  print("Oops!")

输出：
Not True
Alright
False
True
True
False
False
False
False
True
Yeah!
Oops!
