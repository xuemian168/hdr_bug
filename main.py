from PIL import Image
import numpy as np

def convert_to_hdr(input_image_path, output_image_path):
    # 打开输入图像
    img = Image.open(input_image_path).convert('RGB')
    
    # 将图像转换为numpy数组
    img_array = np.array(img) / 255.0  # 归一化到[0, 1]范围

    # 应用PQ EOTF转换
    def pq_eotf(x):
        return np.where(x <= 0.001, x * 12.0, ((x ** (1 / 2.4)) * 1.099) - 0.099)

    # 应用PQ EOTF到每个像素
    hdr_array = np.clip(pq_eotf(img_array), 0, 1)

    # 将HDR数组转换回图像，使用8位深度
    hdr_image = Image.fromarray((hdr_array * 255).astype(np.uint8))  # 使用8位深度

    # 设置色彩配置文件
    icc_profile_path = 'extracted.icc'
    with open(icc_profile_path, 'rb') as f:
        icc_profile = f.read()  # 读取ICC配置文件为字节对象

    # 保存图像时指定ICC配置文件
    hdr_image.save(output_image_path, icc_profile=icc_profile)

# 使用示例
input_path = 'sample.jpg'  # 输入图像路径
output_path = 'output_hdr_image.png'  # 输出HDR图像路径
convert_to_hdr(input_path, output_path)