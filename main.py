# import os
# import sys
# from pathlib import Path
# from pydoc_markdown.interfaces import Context
# from docspec import Module
# from pydoc_markdown.contrib.loaders.python import PythonLoader
# from pydoc_markdown.contrib.renderers.markdown import MarkdownRenderer


# # --- Configuration ---
# SEARCH_PATH = ['UnrealPythonAPI/unreal']
# MODULE_NAME = 'unreal'
# OUTPUT_DIR = Path('docs/api')
# INDEX_FILENAME = 'index.md'
# # --- End Configuration ---

# def get_module_members(module: Module):
#     """Extracts members (classes, functions, variables) from a module."""
#     members = []
#     members.append(module.members[84])
#     # for i in range(len(module.members)):
#     #     member = module.members[84]
#     #     if member.is_class or member.is_function or member.is_variable:
#     #         members.append(member)
#     #         module.members[i] = None  # Remove from original list to avoid duplicates
#     # if hasattr(module, 'classes'):
#     #     members.extend(module.classes or [])
#     # if hasattr(module, 'functions'):
#     #     members.extend(module.functions or [])
#     # if hasattr(module, 'variables'):
#     #     members.extend(module.variables or [])
#     return members

# def main():
#     context = Context(directory='.')
#     # loader = PythonLoader(search_path=SEARCH_PATH, module_names=[MODULE_NAME])
#     loader = PythonLoader(search_path=SEARCH_PATH)
#     renderer = MarkdownRenderer(render_module_header=False, 
#                                 render_toc=True, # Add TOC to individual files
#                                 # classdef_code_render_style='folded', # Fold class code blocks
#                                 # funcdef_code_render_style='folded' # Fold function code blocks
#                                 )

#     loader.init(context)
#     renderer.init(context)

#     modules = list(loader.load())
#     # print(modules)

#     if not modules:
#         print(f"Error: No modules found in {SEARCH_PATH} for module '{MODULE_NAME}'.", file=sys.stderr)
#         sys.exit(1)

#     # Ensure output directory exists
#     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

#     index_content = f"# {MODULE_NAME} API Reference\n\n"
#     module_links = []

#     # Assuming the first loaded module is the one we want ('unreal')
#     unreal_module = modules[0]

#     # Generate individual files for top-level members
#     members = get_module_members(unreal_module)

#     if not members:
#         print(f"Warning: No classes or functions found in module '{unreal_module.name}'.", file=sys.stderr)

#     for member in members:
#         member_name = member.name
#         # Sanitize filename (basic example, might need more robust handling)
#         filename = f"{member_name.replace(' ', '_').replace('.', '_')}.md"
#         filepath = OUTPUT_DIR / filename
        
#         try:
#             # Render only the specific member
#             # Note: pydoc-markdown's default renderer might not directly support rendering
#             # a single member easily. We render the whole module but might need 
#             # custom rendering logic for true isolation if this is too slow/large.
#             # For now, we render the member within the context of its module.
#             # A workaround is to render the whole module and potentially filter later,
#             # or adjust the renderer config if possible.
#             # Let's try rendering just the member by creating a temporary module list.
#             # 根据成员类型创建临时模块
#             classes = [member] if member.is_class else []
#             functions = [member] if member.is_function else []
#             variables = [member] if member.is_variable else []
            
#             temp_module = Module(
#                 name=unreal_module.name,
#                 docstring=unreal_module.docstring,
#                 location=unreal_module.location,
#                 classes=classes,
#                 functions=functions,
#                 variables=variables,
#                 submodules=[]
#             )
            
#             markdown_content = renderer.render_to_string([temp_module])
            
#             with open(filepath, 'w', encoding='utf-8') as f:
#                 f.write(markdown_content)
#             print(f"Generated: {filepath}")
#             module_links.append(f"- [{member_name}]({filename})")
#         except Exception as e:
#             print(f"Error rendering member '{member_name}' to {filepath}: {e}", file=sys.stderr)

#     # Generate index file
#     index_content += "\n".join(sorted(module_links))
#     index_filepath = OUTPUT_DIR / INDEX_FILENAME
#     with open(index_filepath, 'w', encoding='utf-8') as f:
#         f.write(index_content)
#     print(f"Generated index: {index_filepath}")

# if __name__ == "__main__":
#     main()

# 生成 Markdown 文档
# 使用 pydoc-markdown 库将 UnrealPythonAPI/unreal 目录下的 Python 存根文件
# 解析并渲染为 Markdown 格式，保存到 docs/api/api.md。

from pathlib import Path
from pydoc_markdown.interfaces import Context
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.contrib.renderers.markdown import MarkdownRenderer

# 创建 pydoc-markdown 上下文，directory 指定项目根目录作为工作目录
context = Context(directory='.')

# 配置 Python 加载器，search_path 指定存根文件所在目录
# 加载器会递归扫描该路径下的所有 .py 文件并解析其中的类、函数、变量定义
loader = PythonLoader(search_path=[r'UnrealPythonAPI/unreal'])

# 配置 Markdown 渲染器
# render_module_header=False: 不渲染模块级标题（如 "# unreal"），只输出成员内容
renderer = MarkdownRenderer(render_module_header=False)

# 初始化加载器和渲染器，绑定到同一上下文
loader.init(context)
renderer.init(context)

# 加载所有模块，解析 Python 源码为 docspec 数据结构（Module 对象列表）
modules = loader.load()

# 将解析后的模块渲染为 Markdown 字符串
# 生成的内容包含所有类、函数的文档字符串、参数签名、返回值等信息
output = renderer.render_to_string(modules)

# 保存到 docs/raw/api.md
output_path = Path('docs/raw')
output_path.mkdir(parents=True, exist_ok=True)
output_file = output_path / 'api.md'
output_file.write_text(output, encoding='utf-8')
print(f"Generated: {output_file}")