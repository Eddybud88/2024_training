# 创建一个包含魔术师名字的列表  
magicians = ['David Copperfield', 'Penn & Teller', 'Criss Angel', 'David Blaine']  
  
# 定义一个名为show_magicians的函数，该函数接受一个列表作为参数  
def show_magicians(magician_list):  
    # 遍历列表中的每个名字，并打印出来  
    for magician in magician_list:  
        print(magician)  
  
# 定义一个名为make_great的函数，该函数接受一个列表作为参数，并修改列表中的每个名字  
def make_great(magician_list):  
    # 遍历列表中的每个名字，并在其后添加“the Great”  
    for i in range(len(magician_list)):  
        magician_list[i] = magician_list[i] + " the Great"  
  
# 调用make_great函数来修改魔术师列表  
make_great(magicians)  
  
# 调用show_magicians函数来确认魔术师列表确实被修改了  
show_magicians(magicians)

输出：
David Copperfield the Great
Penn & Teller the Great
Criss Angel the Great
David Blaine the Great
