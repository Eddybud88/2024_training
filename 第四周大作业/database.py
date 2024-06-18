import json
import os
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接信息
DATABASE_URI = 'mysql+mysqlconnector://root:Sherry@localhost/autonomous_driving'

# 创建 SQLAlchemy 引擎和声明性基类
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

# 定义数据模型
class DataSet(Base):
    __tablename__ = 'data_set'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_path = Column(String(255))
    image_timestamp = Column(String(255))
    pointcloud_path = Column(String(255))
    point_cloud_stamp = Column(String(255))
    calib_camera_intrinsic_path = Column(String(255))
    calib_lidar_to_camera_path = Column(String(255))
    label_camera_std_path = Column(String(255))
    label_lidar_std_path = Column(String(255))
    image_content = Column(LargeBinary)
    pointcloud_content = Column(LargeBinary)
    calib_camera_intrinsic_content = Column(LargeBinary)
    calib_lidar_to_camera_content = Column(LargeBinary)
    label_camera_std_content = Column(LargeBinary)
    label_lidar_std_content = Column(LargeBinary)

# 函数：创建数据库表格
def create_tables():
    Base.metadata.create_all(engine)

# 函数：读取文件内容
def read_file_content(file_path):
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# 函数：加载 JSON 数据
def load_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON from {file_path}: {e}")
        return None

# 函数：插入数据到数据库
def insert_data(session, data_info):
    for data_dict in data_info['files']:
        new_data = DataSet(
            image_path=data_dict.get('image_path'),
            image_timestamp=data_dict.get('image_timestamp'),
            pointcloud_path=data_dict.get('pointcloud_path'),
            point_cloud_stamp=data_dict.get('point_cloud_stamp'),
            calib_camera_intrinsic_path=data_dict.get('calib_camera_intrinsic_path'),
            calib_lidar_to_camera_path=data_dict.get('calib_lidar_to_camera_path'),
            label_camera_std_path=data_dict.get('label_camera_std_path'),
            label_lidar_std_path=data_dict.get('label_lidar_std_path'),
            image_content=read_file_content(data_dict.get('image_path')),
            pointcloud_content=read_file_content(data_dict.get('pointcloud_path')),
            calib_camera_intrinsic_content=read_file_content(data_dict.get('calib_camera_intrinsic_path')),
            calib_lidar_to_camera_content=read_file_content(data_dict.get('calib_lidar_to_camera_path')),
            label_camera_std_content=read_file_content(data_dict.get('label_camera_std_path')),
            label_lidar_std_content=read_file_content(data_dict.get('label_lidar_std_path')),
        )
        session.add(new_data)

# 主函数
def main():
    # 创建数据库表格
    create_tables()

    # 加载 JSON 数据
    json_file_path = 'C:\\Users\\admin\\Desktop\\single-vehicle-side-example\\data_info.json'
    data_info = load_json_data(json_file_path)

    if data_info:
        Session = sessionmaker(bind=engine)
        session = Session()

        # 插入数据到数据库
        insert_data(session, data_info)

        # 提交更改并关闭会话
        session.commit()
        session.close()
    else:
        print("Failed to load JSON data.")

if __name__ == "__main__":
    main()
