import re
import traceback
from typing import Dict
import json
import os


def readFile(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        content = file.read()
    return content

def readJson(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise



def sanitize_filename(filename):
    """
    将文件名中不能作为文件名的字符替换为下划线 _
    :param filename: 原始文件名
    :return: 清理后的文件名
    """
    # 定义不允许出现在文件名中的字符
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'  # 包括控制字符

    # 使用正则表达式替换
    sanitized_filename = re.sub(invalid_chars, '_', filename)

    return sanitized_filename


def load_prompt_template(template_path: str) -> Dict:
    """加载审查提示模板"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return {"prompt": content}
    except Exception as e:
        raise


def append_content(title, file_path, content):
    dir = os.path.dirname(file_path)
    if not os.path.exists(dir):
        os.makedirs(dir)

    """将内容追加到文件末尾"""
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            if title:
                file.write('\n' + title + ':\n')
            file.write(content + '\n')
    except Exception as e:
        raise


def to_string(obj):
    attributes_string = ""
    for key, value in vars(obj).items():
        if not key.startswith("__"):
            attributes_string += f"{key}: {value}\n"
    return attributes_string


