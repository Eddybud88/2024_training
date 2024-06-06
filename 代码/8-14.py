def make_car(manufacturer, model, **kwargs):  
    """  
    创建一个包含汽车信息的字典。  
    制造商和型号是必需的，其他信息作为关键字实参提供。  
    """  
    car_info = {  
        'manufacturer': manufacturer,  
        'model': model  
    }  
    # 将kwargs中的所有键值对添加到car_info字典中  
    car_info.update(kwargs)  
    return car_info  
  
# 调用函数并打印返回的字典  
car = make_car('Subaru', 'Outback', color='blue', tow_package=True)  
print(car)

输出：
{'manufacturer': 'Subaru', 'model': 'Outback', 'color': 'blue', 'tow_package': True}
