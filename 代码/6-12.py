# 创建一个用于存储外星人的空列表  
aliens = []  
  
# 创建30个绿色的外星人  
# 我们还添加了'name'和'type'两个新的键  
for alien_number in range(30):  
    new_alien = {  
        'name': f'Alien_{alien_number+1}',  # 给每个外星人一个唯一的名称  
        'color': 'green',  
        'type': 'Basic',  # 假设所有外星人的类型都是'Basic'  
        'points': 5,  
        'speed': 'slow',  
        'status': 'alive'  # 假设所有外星人在开始时都是存活的  
    }  
    aliens.append(new_alien)  
  
# 显示前五个外星人  
for alien in aliens[:5]:  
    # 使用更清晰的格式打印外星人信息  
    print(f"Name: {alien['name']}, Color: {alien['color']}, Type: {alien['type']}, Points: {alien['points']}, Speed: {alien['speed']}, Status: {alien['status']}")  
print("...")  
  
# 显示创建了多少个外星人  
print("Total number of aliens:", len(aliens))

输出：
Name: Alien_1, Color: green, Type: Basic, Points: 5, Speed: slow, Status: alive
Name: Alien_2, Color: green, Type: Basic, Points: 5, Speed: slow, Status: alive
Name: Alien_3, Color: green, Type: Basic, Points: 5, Speed: slow, Status: alive
Name: Alien_4, Color: green, Type: Basic, Points: 5, Speed: slow, Status: alive
Name: Alien_5, Color: green, Type: Basic, Points: 5, Speed: slow, Status: alive
...
Total number of aliens: 30
