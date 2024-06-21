from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, LargeBinary

# 创建数据库连接
DATABASE_URI = 'mysql+mysqlconnector://root:Sherry@localhost/autonomous_driving'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

# 定义数据模型类
class Data(Base):
    __tablename__ = 'data_set3'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_path = Column(String(255))
    image_timestamp = Column(String(20))
    pointcloud_path = Column(String(255))
    point_cloud_stamp = Column(String(20))
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

# 创建会话（Session）
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.get("/data/image/{image_path:path}")
async def get_data_by_image_path(image_path: str):
    print(f"Received request for image path: {image_path}")
    data = session.query(Data).filter(Data.image_path == image_path).first()
    if data:
        print(f"Found data for image path: {data.image_path}")
        return {
            "image_path": data.image_path,
            "image_timestamp": data.image_timestamp,
            "pointcloud_path": data.pointcloud_path,
            "point_cloud_stamp": data.point_cloud_stamp,
            "calib_camera_intrinsic_path": data.calib_camera_intrinsic_path,
            "calib_lidar_to_camera_path": data.calib_lidar_to_camera_path,
            "label_camera_std_path": data.label_camera_std_path,
            "label_lidar_std_path": data.label_lidar_std_path,
            "calib_camera_intrinsic_content": data.calib_camera_intrinsic_content.decode('utf-8') if data.calib_camera_intrinsic_content else None,
            "calib_lidar_to_camera_content": data.calib_lidar_to_camera_content.decode('utf-8') if data.calib_lidar_to_camera_content else None,
            "label_camera_std_content": data.label_camera_std_content.decode('utf-8') if data.label_camera_std_content else None,
            "label_lidar_std_content": data.label_lidar_std_content.decode('utf-8') if data.label_lidar_std_content else None,
            "image_content": f"file:///C:/Users/admin/Desktop/single-vehicle-side-example/image/000004.jpg" if data.image_path else None,

        }
    else:
        print("Data not found")
        raise HTTPException(status_code=404, detail="Data not found")

@app.get("/files/{file_path:path}")
async def get_file(file_path: str):
    full_path = f"C:\\Users\\admin\\Desktop\\single-vehicle-side-example/{file_path}"
    if os.path.exists(full_path):
        return FileResponse(full_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

# 启动 FastAPI 服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
