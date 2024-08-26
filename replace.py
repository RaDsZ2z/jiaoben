#替换字符串的脚本
#coding=utf-8
import os
def replace_string_in_file(file_path, old_str, new_str):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace(old_str, new_str)
    with open(file_path, 'w') as file:
        file.write(content)

def traverse_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            replace_string_in_file(file_path,"字符串1","字符串4")
traverse_folder('.')
