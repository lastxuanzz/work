import base64
import gzip
from io import BytesIO

# 用变量保存base64编码后的字符串
encoded_str = \
"H4sIAEn2JWgC/8tIzcnJBwCGphA2BQAAAA=="

# 解码并解压
decoded_bytes = base64.b64decode(encoded_str)
with gzip.GzipFile(fileobj=BytesIO(decoded_bytes)) as f:
    decoded_str = f.read().decode('utf-8')

# 打印解码后的字符串
print(decoded_str)
