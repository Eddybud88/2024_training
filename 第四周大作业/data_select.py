from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
import mysql.connector
import os

app = FastAPI()

# 数据库连接配置
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Sherry",
    "database": "autonomous_driving"
}

# 查询请求模型
class ImageQuery(BaseModel):
    image_filename: str

# 连接到 MySQL 数据库
def connect_to_db():
    return mysql.connector.connect(**db_config)

# 根据文件名查询相关数据
@app.post("/query/")
async def query_data(image_query: ImageQuery):
    image_filename = image_query.image_filename
    db = connect_to_db()
    cursor = db.cursor(dictionary=True)

    try:
        # 查询文件路径
        query = """
        SELECT file_path FROM data_table WHERE file_path LIKE %s
        """
        cursor.execute(query, (f"%{image_filename}%",))
        results = cursor.fetchall()

        if not results:
            raise HTTPException(status_code=404, detail="Image not found")

        data = {
            "lidar_data": [],
            "calibration_data": [],
            "image_url": f"http://localhost:8002/download/{image_filename}"
        }

        for row in results:
            file_path = row["file_path"]
            if file_path.startswith("lidar/") and file_path.endswith(".json"):
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data["lidar_data"].append(json.load(json_file))
            elif file_path.startswith("calib/") and file_path.endswith(".json"):
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data["calibration_data"].append(json.load(json_file))

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    finally:
        cursor.close()
        db.close()

# 提供图片下载链接
@app.get("/download/{image_filename}")
async def download_image(image_filename: str):
    image_dir = r'C:\\Users\\admin\\Desktop\\single-vehicle-side-example\\image'
    image_path = os.path.join(image_dir, image_filename)

    if os.path.exists(image_path):
        return FileResponse(image_path, media_type='image/jpeg')
    else:
        raise HTTPException(status_code=404, detail="Image not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)
