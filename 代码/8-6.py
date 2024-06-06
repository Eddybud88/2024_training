def city_country(city, country):  
    """  
    返回一个包含城市和国家的格式化字符串。  
  
    参数:  
    city (str): 城市的名称  
    country (str): 国家名称  
  
    返回:  
    str: 格式为 "City, Country" 的字符串  
    """  
    return f"{city}, {country}"  
  
# 使用三个城市-国家对调用 city_country() 函数并打印结果  
city_1 = "Santiago"  
country_1 = "Chile"  
print(city_country(city_1, country_1))  
  
city_2 = "Tokyo"  
country_2 = "Japan"  
print(city_country(city_2, country_2))  
  
city_3 = "London"  
country_3 = "United Kingdom"  
print(city_country(city_3, country_3))

输出：
Santiago, Chile  
Tokyo, Japan  
London, United Kingdom
