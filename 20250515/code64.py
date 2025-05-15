import base64
import gzip
from io import BytesIO
import json

# 读取 json 文件内容
with open('test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 转为字符串
json_str = json.dumps(data, ensure_ascii=False)

# utf-8 编码
raw_bytes = json_str.encode('utf-8')

# gzip 压缩
buf = BytesIO()
with gzip.GzipFile(fileobj=buf, mode='wb') as f:
    f.write(raw_bytes)
gzipped_bytes = buf.getvalue()

# base64 编码
encoded_str = base64.b64encode(gzipped_bytes).decode('utf-8')

print(encoded_str)
