# 已有的字典  
person_info1 = {    
    'first_name': 'Eddy',    
    'last_name': 'Bud',    
    'age': 21,    
    'city': 'Wuhan'    
}  
  
# 创建两个新的字典来表示人  
person_info2 = {    
    'first_name': 'Petty',    
    'last_name': 'Smith',    
    'age': 28,    
    'city': 'New York'    
}  
  
person_info3 = {    
    'first_name': 'Boris',    
    'last_name': 'Johnson',    
    'age': 35,    
    'city': 'Los Angeles'    
}  
  
# 将这三个字典存储在一个名为 people 的列表中  
people = [person_info1, person_info2, person_info3]  
  
# 遍历这个列表，将其中每个人的所有信息都打印出来  
for person in people:  
    for key, value in person.items():    
        print(f'{key}: {value}')  
    print()  # 打印一个空行以分隔不同人的信息

输出：
first_name: Eddy
last_name: Bud
age: 21
city: Wuhan

first_name: Petty
last_name: Smith
age: 28
city: New York

first_name: Boris
last_name: Johnson
age: 35
city: Los Angeles
