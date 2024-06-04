favorite_languages = {  
    'jen': 'python',  
    'sarah': 'c',  
    'edward': 'ruby',  
    'phil': 'python',  
}  
  
# 新的人员名单，包括已参与和未参与调查的人  
people_to_survey = ['jen', 'sarah', 'edward', 'phil', 'mike', 'emily', 'tyler']  
  
# 遍历人员名单  
for person in people_to_survey:  
    # 检查这个人是否已经在字典中  
    if person in favorite_languages:  
        print(f"{person.title()} 已经在调查中，感谢您的参与！")  
    else:  
        print(f"欢迎 {person.title()} 参与我们的调查！")

  输出：
Jen 已经在调查中，感谢您的参与！
Sarah 已经在调查中，感谢您的参与！
Edward 已经在调查中，感谢您的参与！
Phil 已经在调查中，感谢您的参与！
欢迎 Mike 参与我们的调查！
欢迎 Emily 参与我们的调查！
欢迎 Tyler 参与我们的调查！
