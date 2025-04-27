# 项目规则

## 项目目标

本项目旨在使用 `pydoc-markdown` 工具将 `UnrealPythonAPI` 目录下的 Python 代码（主要是 Unreal Engine 的 Python API 存根）转换为 Markdown 格式的文档。

## 规则详情

为了确保项目顺利进行并生成高质量的文档，请遵循以下规则：

### 1. 代码风格

- **一致性**: 保持代码风格一致。虽然存根文件可能不完全遵循 PEP 8，但新增或修改的代码应尽量保持简洁和可读。
- **存根实现**: 函数和方法体可以使用 `pass` 或 `...` 作为占位符。

### 2. 文档字符串 (Docstrings)

- **必要性**: 所有公共模块、类、函数和方法都必须包含文档字符串。
- **格式**: 推荐使用 Google 风格的文档字符串，以便 `pydoc-markdown` 能正确解析。
- **内容**: 文档字符串应清晰地描述对象的功能、参数、返回值和可能引发的异常。

### 3. 目录结构

- **代码位置**: 所有 Unreal Engine Python API 存根文件必须放置在 `UnrealPythonAPI` 目录下。
- **模块组织**: 保持与 Unreal Engine 官方 Python API 相似的模块结构。

### 4. 依赖管理

- **核心依赖**: 项目的核心依赖是 `pydoc-markdown`，已在 `pyproject.toml` 中定义。
- **环境**: 推荐使用虚拟环境（如 `.venv`）管理项目依赖。

### 5. 文档生成

- **工具**: 使用 `pydoc-markdown` 生成 Markdown 文档。
- **执行**: 可以通过多种方式生成文档：
    - **使用 `main.py` 脚本 (推荐)**: 运行项目根目录下的 `main.py` 脚本。
      ```bash
      python main.py > documentation.md
      ```
    - **使用 `pydoc-markdown` CLI**: 直接调用命令行工具 <mcreference link="https://niklasrosenstein.github.io/pydoc-markdown/usage/cli-and-api/" index="0">0</mcreference>。
      ```bash
      # 示例：生成单个模块的文档并包含TOC
      pydoc-markdown -I UnrealPythonAPI -m unreal --render-toc > unreal_module.md
      ```
    - **使用 `pydoc-markdown` API**: 在 Python 脚本中调用其 API <mcreference link="https://niklasrosenstein.github.io/pydoc-markdown/usage/cli-and-api/" index="0">0</mcreference>。
      ```python
      from pydoc_markdown import PydocMarkdown
      
      session = PydocMarkdown()
      session.loaders[0].search_path = ["UnrealPythonAPI"]
      # 可以根据需要配置 session.renderer 等
      markdown_content = session.renderer.render_to_string(session.process(session.load_modules()))
      print(markdown_content)
      ```
- **配置**: 
    - `main.py` 中配置了 `pydoc-markdown` 的加载器和渲染器。如有需要，可调整其配置。
    - CLI 方式可以通过命令行参数或 YAML 配置文件进行配置 <mcreference link="https://niklasrosenstein.github.io/pydoc-markdown/usage/cli-and-api/" index="0">0</mcreference>。

### 6. 贡献与维护

- **准确性**: 确保添加或修改的 API 存根与实际的 Unreal Engine Python API 签名一致。
- **更新**: 随着 Unreal Engine 版本的更新，及时维护和补充 API 存根。