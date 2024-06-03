# 2.1 hello world
message = "hello world!";
print(message)

hello world!

# 2.2 变量
message= "hello world!";  
print(message)  

hello world!

# 2.3 字符串  
# 大小写
name = "ada wong"
print(name.title())  # 首字母大写

Ada Wong

name  =  "Ada  Wong"
print(name.upper()) # 全大写
print(name.lower()) # 全小写

ADA WONG
ada wong

# 合并拼接
first_name  =  "Ada"
last_name  =  "Wong"
full_name  =  first_name  +  "  "  +  last_name 
print(full_name)

Ada  Wong

#换行与空白
print("\tAda")

 Ada

print("Games:\n\tResident Evil\n\t\Ada wong")
Games:
      Ressident Evil
      Ada wong

# 删除空白
test=" Ada Wong "
test
' Ada Wong '
test.rstrip() #删去最后空格
' Ada Wong'
test.rstrip() #删去最前空格
'Ada Wong '
test.strip() #删去两端空格
'Ada Wong'

# 2.4 数字
# 四则运算
4 + 5
9

5 - 4
1

5 * 4
20

5 / 4
1.25

5 ** 4
625

# str()应用
age=21
message="Victor, aged" + " " + str(age) + " " + ", is a real genius!" 
print(message)

Victor, aged 21 , is a real genius!
