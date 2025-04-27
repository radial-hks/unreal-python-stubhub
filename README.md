# Unreal Python StubHub

本项目旨在使用 `pydoc-markdown` 工具将 `UnrealPythonAPI` 目录下的 Python 代码（主要是 Unreal Engine 的 Python API 存根）转换为 Markdown 格式的文档。

## 项目目标

为 Unreal Engine 的 Python API 提供类型存根，并通过 `pydoc-markdown` 自动生成结构清晰、易于导航的 Markdown 文档。

## 项目规则

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
- **模块组织**: 保持与 Unreal Engine 官方 Python API 相似的模块结构（例如，所有内容都在 `unreal` 模块下）。
- **文档输出**: 生成的 Markdown 文档位于 `docs/api/` 目录下。

### 4. 依赖管理

- **核心依赖**: 项目的核心依赖是 `pydoc-markdown`，已在 `pyproject.toml` 中定义。
- **环境**: 推荐使用虚拟环境（如 `.venv`）管理项目依赖。
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Linux/macOS
  # 或者
  .venv\Scripts\activate  # Windows
  pip install -e .
  ```

### 5. 文档生成

- **工具**: 使用 `pydoc-markdown` 结合自定义脚本 `main.py` 生成 Markdown 文档。
- **执行 (推荐)**: 运行项目根目录下的 `main.py` 脚本。该脚本会自动处理 `UnrealPythonAPI` 目录下的 `unreal` 模块，并将每个顶级类和函数的文档分别生成到 `docs/api/` 目录下的独立 Markdown 文件中，同时创建一个 `docs/api/index.md` 文件作为入口索引。
  ```bash
  python main.py
  ```
  执行后，请查看 `docs/api/` 目录以获取生成的文档。

- **其他执行方式**: 
    - **使用 `pydoc-markdown` CLI**: 直接调用命令行工具。这对于快速生成单个模块或进行特定配置测试可能有用，但推荐使用 `main.py` 以获得拆分后的文档结构。
      ```bash
      # 示例：生成 unreal 模块的完整文档（非拆分）
      pydoc-markdown -I UnrealPythonAPI -m unreal --render-toc > unreal_module_full.md
      ```
    - **使用 `pydoc-markdown` API**: 在其他 Python 脚本中调用其 API。`main.py` 就是一个使用 API 的例子。

- **配置**: 
    - `main.py` 中配置了 `pydoc-markdown` 的加载器和渲染器，包括搜索路径、目标模块、输出目录 (`docs/api`) 和渲染选项（如折叠代码块、生成TOC）。如有需要，可直接修改 `main.py` 中的配置变量。
    - CLI 方式可以通过命令行参数或 YAML 配置文件进行配置。

### 6. 贡献与维护

- **准确性**: 确保添加或修改的 API 存根与实际的 Unreal Engine Python API 签名一致。
- **完整性**: 鼓励补充缺失的 API 存根和文档字符串。
- **更新**: 随着 Unreal Engine 版本的更新，及时维护和补充 API 存根。

## 查看文档

生成文档后，可以从 `docs/api/index.md` 文件开始浏览，该文件包含了指向各个 API 模块文档的链接。