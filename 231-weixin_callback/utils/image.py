from PIL import Image
from io import BytesIO


def is_webp(path: str):
    return path.endswith('.webp')


def webp2png(webp_binary_data):
    # 从WebP二进制数据创建Pillow图像对象
    webp_image = Image.open(BytesIO(webp_binary_data))

    # 创建一个内存缓冲区来保存PNG二进制数据
    png_buffer = BytesIO()

    # 将图像以PNG格式保存到内存缓冲区
    webp_image.save(png_buffer, format="PNG")

    # 获取PNG二进制数据
    png_binary_data = png_buffer.getvalue()

    return png_binary_data
