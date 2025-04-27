import os
import re

def sanitize_filename(name):
    # 处理非法文件名字符，简单替换空格和非法字符
    name = name.strip()
    name = re.sub(r'[\\/*?:"<>|]', '_', name)
    return name

def split_markdown_by_h2(input_path, output_dir):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则按二级标题分割，同时保留标题
    parts = re.split(r'(\n[#]{2}\s.+)', content)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # parts[0] 是分割前的内容（可能是一级标题、前言），忽略
    for i in range(1, len(parts), 2):
        h2_title = parts[i].strip()  # 例如 ## 第二章
        body = parts[i+1].strip() if i+1 < len(parts) else ''
        
        # 取标题内容（去掉"## "前缀）
        title_text = h2_title.lstrip('#').strip()
        filename = sanitize_filename(title_text) + '.md'
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            # 可以选择把标题也写回去，或者只保存内容
            f.write(h2_title + '\n\n' + body)

    print(f"分割完成！文件输出到: {output_dir}")

# 示例调用
input_markdown = 'api.md'  # 原Markdown路径
output_folder = 'docs/api'  # 输出文件夹
split_markdown_by_h2(input_markdown, output_folder)
