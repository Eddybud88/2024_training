def print_models(unprinted_designs, completed_models):  
    """  
    模拟打印每个设计，直到没有未打印的设计为止  
    打印每个设计后，都将其移到列表completed_models中  
    """  
    while unprinted_designs:  
        current_design = unprinted_designs.pop()  
  
        # 模拟根据设计制作3D打印模型的过程  
        print("Printing model: " + current_design)  
        completed_models.append(current_design)


# 导入 printing_functions.py 模块中的 print_models 函数  
from printing_functions import print_models  
  
# 示例数据  
unprinted_designs = ['design1', 'design2', 'design3']  
completed_models = []  
  
# 调用 print_models 函数  
print_models(unprinted_designs, completed_models)  
  
# 打印打印完成的模型列表  
print("The following models have been printed:")  
for model in completed_models:  
    print(model)
