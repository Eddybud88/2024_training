# user_profile.py  
  
def build_profile(first, last, **user_info):  
    """创建一个字典，其中包含我们知道的有关用户的一切"""  
    profile = {}  
    profile['first_name'] = first  
    profile['last_name'] = last  
    for key, value in user_info.items():  
        profile[key] = value  
    return profile  
  
# 调用build_profile()函数来创建你的简介  
user_profile = build_profile('Albert', 'Einstein',  
                             location='Princeton',  
                             field='Physics',  
                             hobbies=['Violin', 'Sailing'])  
  
# 打印你的简介  
print(user_profile)

输出：
