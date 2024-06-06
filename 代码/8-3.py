def make_shirt(size, text):  
    """  
    创建一个T恤的概述句子  
  
    参数:  
    size (str): T恤的尺码  
    text (str): 要印在T恤上的字样  
  
    返回:  
    None（此函数直接打印结果，不返回任何值）  
    """  
    # 构造并打印句子  
    print(f"已为您制作了尺码为 {size} 的T恤，并印有字样：'{text}'。")  
  
# 位置实参调用
make_shirt("XL", "I love Python")

# 使用关键字实参调用函数  
make_shirt(text="Python编程", size="XL")
输出：
已为您制作了尺码为 XL 的T恤，并印有字样：'I love Python'。
已为您制作了尺码为 XL 的T恤，并印有字样：'Python编程'。
