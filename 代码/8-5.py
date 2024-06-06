def describe_city(city, country="United States"):  
    """  
    描述一座城市及其所属国家。  
  
    参数:  
    city (str): 城市的名字  
    country (str, optional): 城市所属的国家，默认为'United States'  
  
    返回:  
    None（此函数直接打印结果，不返回任何值）  
    """  
    # 构造并打印句子  
    print(f"{city} is in {country}.")  
  
# 调用函数来描述城市  
# 1. 雷克雅未克（Reykjavik）在冰岛（Iceland），不属于默认国家  
describe_city("Reykjavik", "Iceland")  
  
# 2. 纽约（New York）在美国（United States），使用默认值  
describe_city("New York")  
  
# 3. 巴黎（Paris）在法国（France），不属于默认国家  
describe_city("Paris", "France")

输出：
Reykjavik is in Iceland.  
New York is in United States.  
Paris is in France.
