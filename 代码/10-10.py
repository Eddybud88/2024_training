import os  
  
# 下载的文件都放在当前工作目录的'gutenberg_books'文件夹下  
books_dir = 'gutenberg_books'  
  
# 遍历目录中的文件  
for filename in os.listdir(books_dir):  
    if filename.endswith('.txt'):  # 确保是文本文件  
        file_path = os.path.join(books_dir, filename)  
        with open(file_path, 'r', encoding='utf-8') as file:  
            # 读取文件内容  
            content = file.read()  
            # 将内容转换为小写  
            content_lower = content.lower()  
            # 计算'the'出现的次数  
            count_the = content_lower.count('the')  
            # 打印结果  
            print(f"在文件 {filename} 中，单词 'the' 出现了 {count_the} 次。")
