import json
import os
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL数据库连接URI
DATABASE_URI = 'mysql+mysqlconnector://root:Sherry@localhost/autonomous_driving'

# 创建数据库引擎
engine = create_engine(DATABASE_URI, echo=True)

# 声明基类
Base = declarative_base()

# 定义数据模型类
class Data(Base):
    __tablename__ = 'data_set'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 首先按照id定义表
# 定义字符串型变量
    image_path = Column(String(255))
    image_timestamp = Column(String(20))
    pointcloud_path = Column(String(255))
    point_cloud_stamp = Column(String(20))
    calib_camera_intrinsic_path = Column(String(255))
    calib_lidar_to_camera_path = Column(String(255))
    label_camera_std_path = Column(String(255))
    label_lidar_std_path = Column(String(255))
    image_content = Column(LargeBinary)
# 定义二进制型变量
    pointcloud_content = Column(LargeBinary)
    calib_camera_intrinsic_content = Column(LargeBinary)
    calib_lidar_to_camera_content = Column(LargeBinary)
    label_camera_std_content = Column(LargeBinary)
    label_lidar_std_content = Column(LargeBinary)

# 创建继承Base基类的数据表
Base.metadata.create_all(engine)

# 读取文件内容或大小
def get_file_content_or_size(file_path):
    full_path = os.path.join('C:\\Users\\admin\\Desktop\\single-vehicle-side-example', file_path)
    try:
        if os.path.exists(full_path):
            if full_path.endswith('.json') or full_path.endswith('.txt'):
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read().encode('utf-8')  # 读取文本文件内容，编码为utf-8字符串
            else:
                size = os.path.getsize(full_path)
                content = str(size).encode('utf-8')  # 其余文件，获取大小并编码为utf-8字符串
        else:
            content = None
    except Exception as e:
        print(f"Error reading file {full_path}: {e}")
        content = None
    return content

# 读取JSON数据
with open('C:\\Users\\admin\\Desktop\\single-vehicle-side-example\\data_info.json', 'r', encoding='utf-8') as f:
    data_list = json.load(f)

# 创建会话，执行数据库中的操作（通过数据库引擎绑定）
Session = sessionmaker(bind=engine)
session = Session()

# 插入数据到数据库
try:
    for data_dict in data_list:
        new_data = Data(
            image_path=data_dict.get('image_path'),
            image_timestamp=data_dict.get('image_timestamp'),
            pointcloud_path=data_dict.get('pointcloud_path'),
            point_cloud_stamp=data_dict.get('point_cloud_stamp'),
            calib_camera_intrinsic_path=data_dict.get('calib_camera_intrinsic_path'),
            calib_lidar_to_camera_path=data_dict.get('calib_lidar_to_camera_path'),
            label_camera_std_path=data_dict.get('label_camera_std_path'),
            label_lidar_std_path=data_dict.get('label_lidar_std_path'),
            image_content=get_file_content_or_size(data_dict.get('image_path')),
            pointcloud_content=get_file_content_or_size(data_dict.get('pointcloud_path')),
            calib_camera_intrinsic_content=get_file_content_or_size(data_dict.get('calib_camera_intrinsic_path')),
            calib_lidar_to_camera_content=get_file_content_or_size(data_dict.get('calib_lidar_to_camera_path')),
            label_camera_std_content=get_file_content_or_size(data_dict.get('label_camera_std_path')),
            label_lidar_std_content=get_file_content_or_size(data_dict.get('label_lidar_std_path'))
        )
        session.add(new_data)
    session.commit()
except Exception as e:
    session.rollback() # 回滚事务，确保数据库不会被部分提交
    print(f"Error occurred: {e}")
finally:
    session.close()
