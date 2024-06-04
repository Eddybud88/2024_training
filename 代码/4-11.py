pizzas = ['Dameile' , 'Bishengke' , 'MrPizza']
friend_pizza = pizzas[:]
pizzas.append('Haokelai')
friend_pizza.append('KFC')
print("My favorite pizzas are:")
for pizza in pizzas:
  print(pizza)
print("My friend’s favorite pizzas are:")
for pizza in friend_pizza:
  print(pizza)

输出：
My favorite pizzas are:
Dameile
Bishengke
MrPizza
Haokelai
My friend’s favorite pizzas are:
Dameile
Bishengke
MrPizza
KFC
