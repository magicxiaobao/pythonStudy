# json 处理
import json

filename = "../file/data.json"

data = {
    "name": "小宝",
    "age": 32
}

# 写json文件

with open(filename, 'w', encoding='utf-8') as myfile:
    json.dump(data, myfile, indent=4)

# 读json文件

with open(filename, 'r', encoding='utf-8') as myfile:
    json_data = json.load(myfile)
    print(json_data)
