from PIL import Image

def extract_icc_profile(image_path, output_path):
    # 打开图像
    img = Image.open(image_path)

    # 提取 ICC 配置文件
    icc_profile = img.info.get('icc_profile')

    if icc_profile:
        # 将 ICC 配置文件写入文件
        with open(output_path, 'wb') as f:
            f.write(icc_profile)
        print(f"ICC profile extracted to {output_path}")
    else:
        print("No ICC profile found.")

# 使用示例
extract_icc_profile('2181481747483570_.pic.jpg', 'extracted.icc')