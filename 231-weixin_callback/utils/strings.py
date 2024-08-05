import re
from urllib.parse import urlparse
import random

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_random_string(length: int) -> str:
    """随机生成 length 长度位数的字符串"""
    result = ''
    for _ in range(length):
        result += random.choice(characters)
    return result


def snake2camel(value: str) -> str:
    """下划线转小驼峰"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), value)


def str2bool(s: str) -> bool:
    """
    如果 s 为 '0', 'n', 'no', 'false' ，返回 False
    其他情况返回 True
    """
    if isinstance(s, bool):
        return s
    return s.lower() not in ('0', 'n', 'no', 'false')


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        # 检查方案（scheme）和网络位置（netloc）是否存在
        return all([result.scheme, result.netloc])
    except:
        return False
