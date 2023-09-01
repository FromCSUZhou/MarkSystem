import os
import json
import datetime


def save_json(file_path,title,field,answer,question,instruction,reference):
    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    data = {
        "title": title,
        "field":field,
        "answer":answer,
        "question":question,
        "instruction":instruction,
        "reference":reference
    }
    file_name = answer[:10] if len(answer) > 10 else datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # 指定要保存的文件路径
    data_collection_json_file_path = os.path.join(file_path,file_name + ".json")
    # 将数据写入 JSON 文件
    with open(data_collection_json_file_path, "w") as json_file:
        json.dump(data, json_file, ensure_ascii=True, indent=4)

def read_json(file_path):
    # 读取 JSON 文件并解析数据
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

def read_delete_json(json_files):
    with open(json_files, "r") as json_file:
        first_json_data = json.load(json_file)
    # 把文件删除
    os.remove(json_files)
    return first_json_data

def delete_json(json_files):
    try:
        os.remove(json_files)
    except:
        print("Cannot remove")
