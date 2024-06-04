my_foods  =  ['pizza',  'falafel',  'carrot  cake']
friend_foods  =  my_foods[:]
print("My  favorite  foods  are:") 
print(my_foods)
for food in my_foods:
  print(food)
print("\nMy  friend's  favorite  foods  are:") 
print(friend_foods)
for food in friend_foods:
  print(food)

输出：
My  favorite  foods  are:
['pizza', 'falafel', 'carrot  cake']
pizza
falafel
carrot  cake

My  friend's  favorite  foods  are:
['pizza', 'falafel', 'carrot  cake']
pizza
falafel
carrot  cake

