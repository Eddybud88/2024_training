import os
import json
import pandas as pd
import numpy as np
from PIL import Image
import open3d as o3d

# 加载data_info.json
def load_data_info(data_info_path):
    with open(data_info_path, 'r') as f:
        data_info = json.load(f)
    return data_info

# 加载校准数据
def load_calibration_data(calib_dir):
    calib_data = {}
    for file in os.listdir(calib_dir):
        if file.endswith(".txt"):
            file_path = os.path.join(calib_dir, file)
            with open(file_path, 'r') as f:
                calib_data[file] = f.read()
    return calib_data

# 加载标签数据
def load_label_data(label_dir):
    label_data = {}
    for file in os.listdir(label_dir):
        if file.endswith(".txt"):
            file_path = os.path.join(label_dir, file)
            with open(file_path, 'r') as f:
                label_data[file] = f.read()
    return label_data

# 加载图像数据
def load_image_data(image_dir):
    image_data = {}
    for file in os.listdir(image_dir):
        if file.endswith(".png") or file.endswith(".jpg"):
            file_path = os.path.join(image_dir, file)
            image_data[file] = Image.open(file_path)
    return image_data

# 加载雷达点云数据
def load_velodyne_data(velodyne_dir):
    velodyne_data = {}
    for file in os.listdir(velodyne_dir):
        if file.endswith(".bin"):
            file_path = os.path.join(velodyne_dir, file)
            velodyne_data[file] = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
    return velodyne_data

# 清洗和预处理数据
def preprocess_and_clean_data(data_info, calib_data, label_data, image_data, velodyne_data):
    # 示例预处理步骤
    # 根据具体需求进行处理和清洗
    cleaned_data = {
        'data_info': data_info,
        'calib_data': calib_data,
        'label_data': label_data,
        'image_data': image_data,
        'velodyne_data': velodyne_data
    }
    return cleaned_data

# 保存清洗后的数据
def save_cleaned_data(cleaned_data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 保存data_info
    with open(os.path.join(output_dir, 'data_info_cleaned.json'), 'w') as f:
        json.dump(cleaned_data['data_info'], f)
    
    # 保存校准数据
    for file, data in cleaned_data['calib_data'].items():
        with open(os.path.join(output_dir, 'calib', file), 'w') as f:
            f.write(data)
    
    # 保存标签数据
    for file, data in cleaned_data['label_data'].items():
        with open(os.path.join(output_dir, 'label', file), 'w') as f:
            f.write(data)
    
    # 保存图像数据
    for file, image in cleaned_data['image_data'].items():
        image.save(os.path.join(output_dir, 'image', file))
    
    # 保存雷达点云数据
    for file, points in cleaned_data['velodyne_data'].items():
        points.tofile(os.path.join(output_dir, 'velodyne', file))
    
    print(f"清洗后的数据已保存到: {output_dir}")

# 主函数
def main():
    data_dir = "single-vehicle-side-example"
    output_dir = "cleaned_data"
    
    # 加载数据
    data_info_path = os.path.join(data_dir, 'data_info.json')
    data_info = load_data_info(data_info_path)
    calib_data = load_calibration_data(os.path.join(data_dir, 'calib'))
    label_data = load_label_data(os.path.join(data_dir, 'label'))
    image_data = load_image_data(os.path.join(data_dir, 'image'))
    velodyne_data = load_velodyne_data(os.path.join(data_dir, 'velodyne'))
    
    print("数据加载完成")
    
    # 预处理和清洗数据
    cleaned_data = preprocess_and_clean_data(data_info, calib_data, label_data, image_data, velodyne_data)
    print("数据预处理和清洗完成")
    
    # 保存处理后的数据
    save_cleaned_data(cleaned_data, output_dir)

# 运行主函数
if __name__ == "__main__":
    main()
