animals = ['dog' , 'cat' , 'fox' , 'lion' , 'tiger']
print("The first three items in the list are:")
for animal in animals[:3]:
	print(animal)
print("Three items from the middle of the list are:")
for animal in animals[1:4]:
	print(animal)
print("The last three items in the list are:")
for animal in animals[-3:]:
	print(animal)

输出：
The first three items in the list are:
dog
cat
fox
Three items from the middle of the list are:
cat
fox
lion
The last three items in the list are:
fox
lion
tiger
