# 创建一个包含魔术师名字的列表  
magicians = ['David Copperfield', 'Penn & Teller', 'Criss Angel', 'David Blaine']  
  
# 定义一个名为show_magicians的函数，该函数接受一个列表作为参数  
def show_magicians(magician_list):  
    # 遍历列表中的每个名字，并打印出来  
    for magician in magician_list:  
        print(magician)  
  
# 调用show_magicians函数，并将魔术师名字列表作为参数传递  
show_magicians(magicians)

输出：
David Copperfield
Penn & Teller
Criss Angel
David Blaine
