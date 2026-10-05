import yaml

def read_yaml(file_path):
    """
    读取yaml配置文件，返回字典数据
    :param file_path: yaml文件路径
    :return: dict
    """
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data
    except Exception as e:
        print(f"读取yaml文件失败：{e}")
        return None
