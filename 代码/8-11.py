# 创建一个包含魔术师名字的列表  
original_magicians = ['David Copperfield', 'Penn & Teller', 'Criss Angel', 'David Blaine']  
  
# 定义一个名为show_magicians的函数，该函数接受一个列表作为参数  
def show_magicians(magician_list):  
    # 遍历列表中的每个名字，并打印出来  
    for magician in magician_list:  
        print(magician)  
  
# 定义一个名为make_great的函数，该函数接受一个列表作为参数，并返回修改后的新列表  
def make_great(magician_list):  
    # 创建一个新的列表来存储修改后的名字  
    great_magicians = []  
    # 遍历原始列表中的每个名字，并在其后添加“the Great”，然后添加到新列表中  
    for magician in magician_list:  
        great_magicians.append(magician + " the Great")  
    # 返回修改后的新列表  
    return great_magicians  
  
# 调用make_great函数来创建包含添加了“the Great”的魔术师名字的新列表  
great_magicians = make_great(original_magicians)  
  
# 使用原始列表调用show_magicians函数  
print("Original magicians:")  
show_magicians(original_magicians)  
  
# 使用修改后的列表调用show_magicians函数  
print("\nMagicians with 'the Great':")  
show_magicians(great_magicians)

输出：
Original magicians:
David Copperfield
Penn & Teller
Criss Angel
David Blaine

Magicians with 'the Great':
David Copperfield the Great
Penn & Teller the Great
Criss Angel the Great
David Blaine the Great
