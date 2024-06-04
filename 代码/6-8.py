dog = {  
    'name': 'Buddy',  
    'type': 'Dog',  
    'owner': 'John Doe'  
}  
  
cat = {  
    'name': 'Whiskers',  
    'type': 'Cat',  
    'owner': 'Jane Smith'  
}  
  
hamster = {  
    'name': 'Hammy',  
    'type': 'Hamster',  
    'owner': 'Alice Johnson'  
}  
  
# 将这些字典存储在一个名为 pets 的列表中  
pets = [dog, cat, hamster]  
  
# 遍历列表并打印每个宠物的信息  
for pet in pets:  
    print(f'Pet Name: {pet["name"]}')  
    print(f'Pet Type: {pet["type"]}')  
    print(f'Owner: {pet["owner"]}')  
    print()  

输出：
Pet Name: Buddy  
Pet Type: Dog  
Owner: John Doe  
  
Pet Name: Whiskers  
Pet Type: Cat  
Owner: Jane Smith  
  
Pet Name: Hammy  
Pet Type: Hamster  
Owner: Alice Johnson
