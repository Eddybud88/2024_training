import requests
import zipfile
import os

# 文件URL
file_url = "https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16177052511510528.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-17T15%3A10%3A26Z%2F604800%2F%2F6ee146b4bfcf9fab887ae2f916f2d3d43a8ffab8e64550b8ecce0050c59920ee"

# 下载文件的本地路径
local_filename = "example.zip"

# 下载文件
with requests.get(file_url, stream=True) as response:
    response.raise_for_status()  # 检查下载是否成功
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

print(f"下载完成: {local_filename}")

# 解压缩文件
with zipfile.ZipFile(local_filename, 'r') as zip_ref:
    zip_ref.extractall("example_data")

print("解压完成")

# 检查解压后的文件
extracted_files = os.listdir("example_data")
print("解压后的文件: ", extracted_files)
