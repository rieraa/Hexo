import pandas as pd
import json
import os

# 读取CSV文件
csv_file = r'.\export_urls.csv'  # 使用原始字符串来表示路径
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

# 指定新的路径
output_file_path = os.path.join(r'D:\Data', "image_data.json")

# 保存 JSON 到指定路径
with open(output_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON 数据已保存到 {output_file_path}")

