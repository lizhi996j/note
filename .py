from sentence_transformers import SentenceTransformer
import os
import requests
import sys
from tqdm import tqdm

def download_file(download_url, save_path):
    try:
        print(f"开始下载: {os.path.basename(save_path)}")
        
        # 设置代理
        proxies = {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890'
        }
        
        # 添加请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # 发送请求并获取文件大小
        response = requests.get(download_url, stream=True, proxies=proxies, headers=headers, timeout=30)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        
        # 使用tqdm显示下载进度
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        
        # 下载文件
        with open(save_path, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                progress_bar.update(size)
        progress_bar.close()
        
        print(f"{os.path.basename(save_path)} 下载完成")
        return True
        
    except Exception as e:
        print(f"下载失败: {str(e)}")
        return False

# 模型文件路径
model_path = "./models/all-MiniLM-L6-v2"
os.makedirs(model_path, exist_ok=True)

# 从官方下载的文件
base_url = "https://sbert.net/models/all-MiniLM-L6-v2.zip"
zip_path = os.path.join(model_path, "model.zip")

# 下载模型
if not os.path.exists(zip_path):
    success = download_file(base_url, zip_path)
    if not success:
        print("模型下载失败")
        sys.exit(1)

# 解压模型
print("解压模型文件...")
import zipfile
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(model_path)

# 删除zip文件
os.remove(zip_path)

# 使用本地模型
print("加载本地模型...")
model = SentenceTransformer(model_path)
print("模型加载完成！")


