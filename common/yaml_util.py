import yaml
import os

def read_yaml(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data=yaml.safe_load(f)
            return data
    except Exception as e:
            print(f"错误{e}")
            return None

def get_test_cases(yaml_data, key_name):
    """
    读取yaml用例，返回 (cases_list, ids_list)
    yaml_data：读取完yaml的字典对象
    key_name：yaml里面的key，例如 "delete_users_data"
    """
    case_list = yaml_data.get(key_name, [])   # 取不到返回空列表，防止None报错
    id_list = [case.get("case_name", "未命名") for case in case_list]
    return case_list, id_list
