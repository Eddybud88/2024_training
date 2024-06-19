import json
import mysql.connector
import os

# 读取 data_info.json 文件
json_file_path = 'C:\\Users\\admin\\Desktop\\single-vehicle-side-example\\data_info.json'
with open(json_file_path, 'r', encoding='utf-8') as file:
    data_info = json.load(file)  # 将 JSON 文件加载为 Python 字典

# 连接到 MySQL 数据库
try:
    db = mysql.connector.connect(
        host="localhost",  # MySQL 服务器地址
        user="root",  # MySQL 用户名
        password="Sherry",  # MySQL 用户密码
        database="autonomous_driving"  # 要连接的数据库名称
    )

    cursor = db.cursor()  # 创建一个游标对象，用于执行 SQL 查询

    # 创建数据表，如果数据表不存在则创建
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_table (
        id INT AUTO_INCREMENT PRIMARY KEY,  # 自动递增的主键
        file_path VARCHAR(255),             # 文件路径
        content LONGTEXT,                   # 文本文件内容
        file_size BIGINT                    # 二进制文件大小
    )
    """)

    # 定义文件类型列表
    text_extensions = ['.json', '.txt']
    binary_extensions = ['.pcd', '.jpg', '.png', '.bin', '.dat']

    # 处理 data_info 中的每个文件
    for item in data_info:
        for key, file_path in item.items():
            if os.path.exists(file_path):  # 检查文件是否存在
                file_type = os.path.splitext(file_path)[-1]

                # 初始化变量以防在数据插入时未定义
                content = None
                file_size = None

                try:
                    # 如果文件是文本文件
                    if file_type in text_extensions:
                        with open(file_path, 'r', encoding='utf-8') as text_file:
                            content = text_file.read()

                    # 如果文件是二进制文件
                    elif file_type in binary_extensions:
                        file_size = os.path.getsize(file_path)

                    # 将文件路径和相应的文件内容或文件大小插入到数据库中
                    cursor.execute("""
                    INSERT INTO data_table (file_path, content, file_size) 
                    VALUES (%s, %s, %s)
                    """, (file_path, content, file_size))

                    db.commit()  # 提交事务，保存更改
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

finally:
    db.close()  # 确保数据库连接在最后关闭

