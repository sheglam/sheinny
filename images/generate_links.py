import os
import pandas as pd

# 本地图片文件夹路径
local_image_folder = r'D:\renamed_images'

# GitHub 图床前缀链接
github_prefix = 'https://raw.githubusercontent.com/sheglam/sheinny/main/images'

# 用于保存链接的列表
links_data = []

# 遍历所有子目录中的文件
for root, dirs, files in os.walk(local_image_folder):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            # 获取文件完整路径
            full_path = os.path.join(root, file)

            # 获取文件名（不含扩展名）作为 SPU
            spu = os.path.splitext(file)[0]

            # 构造链接
            github_url = f'{github_prefix}/{file}'

            # 保存
            links_data.append({'SPU': spu, 'URL': github_url})

# 保存为 Excel
df = pd.DataFrame(links_data)
output_path = os.path.join(local_image_folder, 'image_links.xlsx')
df.to_excel(output_path, index=False)

print(f"✅ 链接已保存到: {output_path}")
