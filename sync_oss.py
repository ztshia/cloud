import os
import oss2

# 配置你的阿里云 OSS 信息
ACCESS_KEY = os.getenv('ALIYUN_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('ALIYUN_ACCESS_KEY_SECRET')
ENDPOINT = 'https://oss-cn-nanjing.aliyuncs.com'
BUCKET_NAME = 'neos'
LOCAL_DIR = '/'

# 初始化 OSS 客户端
auth = oss2.Auth(ACCESS_KEY, SECRET_KEY)
bucket = oss2.Bucket(auth, ENDPOINT, BUCKET_NAME)

# 列出桶内所有对象
for obj in oss2.ObjectIterator(bucket):
    # 构建本地文件路径
    local_path = os.path.join(LOCAL_DIR, obj.key)
    
    # 确保本地目录存在
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    # 下载对象到本地
    bucket.get_object_to_file(obj.key, local_path)