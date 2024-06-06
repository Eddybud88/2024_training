def make_shirt(size="L", text="I love Python"):  
    """  
    创建一个T恤的概述句子  
  
    参数:  
    size (str): T恤的尺码，默认为'L'  
    text (str): 要印在T恤上的字样，默认为'I love Python'  
  
    返回:  
    None（此函数直接打印结果，不返回任何值）  
    """  
    # 构造并打印句子  
    print(f"已为您制作了尺码为 {size} 的T恤，并印有字样：'{text}'。")  
  
# 调用函数来制作T恤  
# 1. 印有默认字样的大号T恤  
make_shirt()  
  
# 2. 印有默认字样的中号T恤  
make_shirt(size="M")  
  
# 3. 印有其他字样的T恤（尺码无关紧要）  
make_shirt(text="Hello, World!")

输出：
已为您制作了尺码为 L 的T恤，并印有字样：'I love Python'。  
已为您制作了尺码为 M 的T恤，并印有字样：'I love Python'。  
已为您制作了尺码为 L 的T恤，并印有字样：'Hello, World!'。
