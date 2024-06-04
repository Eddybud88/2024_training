foods = ('jiaozi' , 'noodles' , 'rice' , 'chicken' , 'beef')
for food in foods:
  print(food)
food[0]='baozi'
foods = ('pork' , 'noodles' , 'pizza' , 'chicken' , 'beef')
for food in foods:
  print(food)

输出：
jiaozi
noodles
rice
chicken
beef
Traceback (most recent call last):
  File "/home/eddybud/name.py", line 4, in <module>
    food[0]='baozi'
    ~~~~^^^
TypeError: 'str' object does not support item assignment
pork
noodles
pizza
chicken
beef

