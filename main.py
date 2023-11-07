import pandas as pd
import json
import os

# 读取CSV文件
csv_file = r'D:\Data\Download\export_urls (4).csv'  # 使用原始字符串来表示路径
df = pd.read_csv(csv_file, sep=',')

# 遍历CSV文件的每一行，逐行生成JSON并输出
json_data = []

for index, row in df.iterrows():
    url = row['url']
    alt = row['object']
    title = row['object']

    image_json = {
        "url": url,
        "alt": alt,
        "title": title
    }

    json_data.append(image_json)

# 保存JSON到桌面
output_file_path = os.path.expanduser("~/Desktop/image_data.json")
with open(output_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON数据已保存到桌面的 {output_file_path}")
