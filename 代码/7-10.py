# 提示用户输入他们梦想的度假胜地  
def survey_dream_destination():  
    destination = input("如果你能去世界上任何一个地方度假，你会去哪里？ ")  
    return destination  
  
# 打印调查结果  
def print_survey_result(destination):  
    print(f"你的梦想度假胜地是：{destination}")  
  
# 调用函数进行调查并打印结果  
dream_place = survey_dream_destination()  
print_survey_result(dream_place)


输出：
如果你能去世界上任何一个地方度假，你会去哪里？ London
你的梦想度假胜地是：London
